from django.contrib.auth.mixins import UserPassesTestMixin
# from django.utils.decorators import method_decorator
# from django.views.generic import TemplateView
from django.urls import reverse_lazy

# def admin_required(function=None):
#     actual_decorator = user_passes_test(
#         lambda u: u.is_authenticated and u.user_type == 'admin',
#         login_url= reverse_lazy('auth-login-basic')
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator

# @method_decorator(admin_required, name='dispatch')
# class AdminOnlyView(TemplateView):
#     template_name = 'admin_template.html'


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'admin'

    def handle_no_permission(self):
        from django.shortcuts import redirect
        return redirect(reverse_lazy('auth-login-basic'))
