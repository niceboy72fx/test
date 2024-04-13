from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from module.account.manager import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    refresh_token_signature = models.CharField(max_length=128, blank= True, default = True)
    gender = models.CharField(max_length=128, blank= True)
 
    
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()
    
    @property
    def full_name(self):
        return f'{self.last_name} + {self.first_name}'
    
    
    def tokens(self):    
        refresh = RefreshToken.for_user(self)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }