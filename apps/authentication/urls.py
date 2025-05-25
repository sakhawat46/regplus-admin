from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    ForgetPasswordView, LoginView, SignUpView, CustomPasswordResetConfirmView,
    PasswordResetDoneView, SignUpApiView, LogInApiView, LogoutView, LogOutView
)


urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="auth-login-basic"),
    path("auth/logput/", LogOutView.as_view(), name="auth-logout-basic"),
    path("auth/signup/", SignUpView.as_view(), name="auth-register-basic"),
    path("auth/forgot_password/", ForgetPasswordView.as_view(), name="auth-forgot-password-basic"),
    path("auth/password_reset_done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('api/auth/register/', SignUpApiView.as_view(), name='register'),
    path('api/auth/login/', LogInApiView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
