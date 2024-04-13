from django.urls import path

from module.account.views import LoginUserView, LogoutApiView, RegisterUserView, VerifyUserEmail
from rest_framework_simplejwt.views import (TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path('login/', LoginUserView.as_view(), name='login-user'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', LogoutApiView.as_view(), name='logout')
]