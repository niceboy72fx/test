from util.otp import send_normal_email
from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=155, min_length=6)
    password=serializers.CharField(max_length=68, write_only=True)
    username=serializers.CharField(max_length=255, read_only=True)
    access_token=serializers.CharField(max_length=255, read_only=True)
    refresh_token=serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password',  'username', 'access_token', 'refresh_token']
        
    def validate(self, attr):
        email = attr.get('email')
        password = attr.get('password')
        request = self.context.get('request')
        find_user = User.objects.filter(email=email).first()
        user = authenticate(request, username=find_user.username, password=password)
        if not user:
            raise AuthenticationFailed("invalid credentials !")
        if not user.is_active:
            raise AuthenticationFailed("Email is not verified")
        token = user.tokens()
        
        return {
            'email': email,
            'username': user.username,
            "access_token":str(token.get('access')),
            "refresh_token":str(token.get('refresh'))
        }
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    re_password = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 're_password']
    
    def validate(self, data):
        password = data.get('password', '')
        re_password = data.get('re_password', '')
        if password != re_password:
            raise serializers.ValidationError("Passwords do not match!")
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['first_name'] + ' ' + validated_data['last_name'],
            phone_number=validated_data.get('phone_number', ''),  # Optional field
            password=validated_data['password'],
        )
        return user
    


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    
    class Meta:
        field = ['refresh_token']
        
        
    def validate(self, request):
        self.token  = request.get('refresh_token')
        return request
    
    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            return {"error": "Token is expired or invalid"}
            