from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    ForgetPasswordView, LoginView, CustomPasswordResetConfirmView,
    PasswordResetDoneView, SignUpApiView, LogInApiView, LogOutApiView, LogOutView, ProfileApiView, SignUpView
)


urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="auth-login-basic"),
    path("auth/signup/", SignUpView.as_view(), name="auth-register-basic"),
    path("auth/logout/", LogOutView.as_view(), name="auth-logout-basic"),
    path("auth/forgot_password/", ForgetPasswordView.as_view(), name="auth-forgot-password-basic"),
    path("auth/password_reset_done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('api/auth/register/', SignUpApiView.as_view(), name='register'),
    path('api/auth/login/', LogInApiView.as_view(), name='login'),
    path('api/auth/logout/', LogOutApiView.as_view(), name='logout'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/profile/', ProfileApiView.as_view(), name='profile'),
]
