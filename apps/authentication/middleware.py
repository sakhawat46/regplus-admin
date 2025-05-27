from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


def admin_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == 'admin',
        login_url= reverse_lazy('auth-login-basic')
    )
    
    if function:
        return actual_decorator(function)
    return actual_decorator

@method_decorator(admin_required, name='dispatch')
class AdminOnlyView(TemplateView):
    template_name = 'admin_template.html'