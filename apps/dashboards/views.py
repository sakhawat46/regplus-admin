from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.utils.decorators import method_decorator
from apps.authentication.middlewares import AdminRequiredMixin


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""

# @method_decorator(admin_required, name='dispatch')
class DashboardsView(TemplateView, AdminRequiredMixin):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
