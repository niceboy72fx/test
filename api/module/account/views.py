from django.shortcuts import render


class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]
    
    
    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data
            return Response(
                {
                    'data':user,
                    'messager': f'OK'
                }
            , status = status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



class LoginUserView(GenericAPIView):
    serializer_class = UserLoginSerializer
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception = True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class LogoutApiView(GenericAPIView):
    serializers_class = LogoutSerializer
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializers_class(data =  request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
   