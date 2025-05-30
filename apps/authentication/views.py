from django.views.generic import TemplateView, View
from django.contrib.auth import logout
from web_project import TemplateLayout
from django.contrib.auth.mixins import LoginRequiredMixin
from web_project.template_helpers.theme import TemplateHelper
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.urls import reverse, reverse_lazy
from urllib.parse import urlencode
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer
from django.contrib import messages
User = get_user_model()







class AuthView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )

        return context


class LoginView(AuthView):
    template_name = 'auth_login_basic.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['email'] = request.session.get('remember_email', '')
        return self.render_to_response(context)


    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        user = authenticate(request=request, email=email, password=password)

        # If authentication failed
        if user is None:
            context = self.get_context_data()
            context["error"] = "Invalid email, username or password."
            context["email"] = email
            return self.render_to_response(context)

        # If authentication succeeded
        if remember_me:
            request.session['remember_email'] = email
        else:
            request.session.pop('remember_email', None)

        login(request, user)
        return redirect('/')

class LogOutView(View, LoginRequiredMixin):
    login_url = reverse_lazy('auth-login-basic')

    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect(reverse('auth-login-basic'))

    def post(self, request):
        return self.get(request)



class SignUpView(AuthView):
    template_name = 'auth_register_basic.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            context = self.get_context_data()
            context["error"] = "Password and Confirm password is Invalid."
            return self.render_to_response(context)

        if User.objects.filter(email=email).exists():
            context = self.get_context_data()
            context["error"] = "Email is already in use."
            return self.render_to_response(context)

        user = User.objects.create_user(email=email, password=password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        return redirect('auth-login-basic')



class ForgetPasswordView(AuthView):
    template_name = 'auth_forgot_password_basic.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        username = request.POST.get('username')
        if username:
            user = User.objects.filter(username=username)[0] if User.objects.filter(username=username).exists() else None
            if user is None:
                memssage='Invalid Username or user not registared.'
        else:
            user = User.objects.filter(email=email)[0] if User.objects.filter(email=email).exists() else None
            if user is None:
                memssage='Invalid Email or user not registared.'

        if user:
                subject = "Password Reset Requested"

                context = self.get_context_data()
                context = {
                    'email': email,
                    'domain': request.META['HTTP_HOST'],
                    'site_name': 'Your Site',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'https' if request.is_secure() else 'http',
                }
                html_message  = render_to_string("emails/password_reset_email.html", context)
                plain_message = strip_tags(html_message)
                try:
                    email = EmailMultiAlternatives(
                        subject=subject,
                        body=plain_message,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[user.email],
                    )
                    email.attach_alternative(html_message, "text/html")
                    email.send()

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('password_reset_done')
        else:
            context = self.get_context_data()
            context["error"] = memssage
            return self.render_to_response(context)

class PasswordResetDoneView(AuthView):
    template_name = 'password_reset_email_send_done.html'
    def get(self, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)


class CustomPasswordResetConfirmView(AuthView):
    template_name = 'password_reset_confirm.html'

    def get_user_from_uidb64(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user


    def post(self, request, *args, **kwargs):
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if new_password1 != new_password2:
            context = self.get_context_data()
            context["error"] = "New Password and Confirm password is Invalid."
            return self.render_to_response(context)

        try:
            uidb64 = kwargs.get('uidb64')
            token = kwargs.get('token')
            user = self.get_user_from_uidb64(uidb64)

            if user and default_token_generator.check_token(user, token):
                user.set_password(new_password1)
                user.save()

                base_url = reverse('auth-login-basic')
                query_string = urlencode({'message': 'Your password has been reset successfully'})
                url = f"{base_url}?{query_string}"
                return redirect(url)
            else:
                context = self.get_context_data()
                context["error"] = "Invalid or expired password reset link."
                return self.render_to_response(context)

        except Exception as e:
            context = self.get_context_data()
            context["error"] = str(e)
            return self.render_to_response(context)





class SignUpApiView(CreateAPIView):
    serializer_class = UserSerializer



class LogInApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LogOutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful"})
        except Exception as e:
            return Response({"detail": str(e)}, status=400)


class ProfileApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
