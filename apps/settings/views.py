from django.views.generic import UpdateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from rest_framework.generics import ListAPIView
from web_project import TemplateLayout
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
from .models import (
    LogoSettings, GeneralSettings, ColorSettings, ContactSettings,
    CurrencySettings, HRMSettings, SMSSettings, SocialSettings, OtherSettings,
    FooterLayout, FooterTop, SocialLinks, SubscribeForm, FooterColumn,
    FooterBottom, FooterCopyright, SEOSettings, PaymentMethod
)
from .forms import (
    LogoSettingsForm, GeneralSettingsForm, ColorSettingsForm,
    ContactSettingsForm, CurrencySettingsForm, HRMSettingsForm,
    SMSSettingsForm, SocialSettingsForm, OtherSettingsForm,
    FooterLayoutForm, FooterTopForm, SocialLinksForm, SubscribeFormForm,
    FooterColumnForm, FooterBottomForm, FooterCopyrightForm,
    SEOSettingsForm, PaymentMethodForm
)
from .serializers import (
    LogoSettingsSerializer, GeneralSettingsSerializer, ColorSettingsSerializer, ContactSettingsSerializer,
    CurrencySettingsSerializer, HRMSettingsSerializer, SMSSettingsSerializer, SocialSettingsSerializer, OtherSettingsSerializer,
    FooterLayoutSerializer, FooterTopSerializer, SocialLinksSerializer, SubscribeFormSerializer, FooterColumnSerializer,
    FooterBottomSerializer, FooterCopyrightSerializer, SEOSettingsSerializer, PaymentMethodSerializer
)





class BaseUpdateView(UpdateView):
    template_name = 'edit.html'
    def get_success_url(self):
        return self.request.path_info

    def form_valid(self, form):
        messages.success(self.request, f"{ self.get_object(self) } Update successful.")
        return super().form_valid(form)

    URL_MAPPING = {
        'settings_dashboard': reverse_lazy('settings_dashboard'),
        'header_footer_dashboard': reverse_lazy('header_footer_dashboard'),
        'seo': reverse_lazy('seo'),
    }

    # def get_success_url(self):
    #     # Check for explicit 'next' parameter first
    #     next_url = self.request.POST.get('next') or self.request.GET.get('next')
    #     if next_url:
    #         return next_url

    #     # Fall back to checking HTTP_REFERER
    #     referer = self.request.META.get('HTTP_REFERER', '')
    #     for pattern, url in self.URL_MAPPING.items():
    #         if pattern in referer:
    #             return url

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

    def get_object(self, queryset=None):
        obj, created = self.model.objects.get_or_create(pk=1)
        return obj

class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context


class SettingsDashboardView(BaseView):
    template_name = 'settings-dashboard.html'

# Individual settings views
class LogoSettingsView(BaseUpdateView):
    model = LogoSettings
    form_class = LogoSettingsForm

class GeneralSettingsView(BaseUpdateView):
    model = GeneralSettings
    form_class = GeneralSettingsForm

class ColorSettingsView(BaseUpdateView):
    model = ColorSettings
    form_class = ColorSettingsForm

class ContactSettingsView(BaseUpdateView):
    model = ContactSettings
    form_class = ContactSettingsForm

class CurrencySettingsView(BaseUpdateView):
    model = CurrencySettings
    form_class = CurrencySettingsForm

class HRMSettingsView(BaseUpdateView):
    model = HRMSettings
    form_class = HRMSettingsForm

class SMSSettingsView(BaseUpdateView):
    model = SMSSettings
    form_class = SMSSettingsForm

class SocialSettingsView(BaseUpdateView):
    model = SocialSettings
    form_class = SocialSettingsForm

class OtherSettingsView(BaseUpdateView):
    model = OtherSettings
    form_class = OtherSettingsForm


# Individual settings views
class HeaderFooterDashboardView(BaseView):
    template_name = 'header-footer-dashboard.html'

class FooterLayoutView(BaseUpdateView):
    model = FooterLayout
    form_class = FooterLayoutForm

class FooterTopView(BaseUpdateView):
    model = FooterTop
    form_class = FooterTopForm

class SocialLinksView(BaseUpdateView):
    model = SocialLinks
    form_class = SocialLinksForm

class SubscribeFormView(BaseUpdateView):
    model = SubscribeForm
    form_class = SubscribeFormForm

class FooterColumnView(BaseUpdateView):
    model = FooterColumn
    form_class = FooterColumnForm

class FooterBottomView(BaseUpdateView):
    model = FooterBottom
    form_class = FooterBottomForm

class FooterCopyrightView(BaseUpdateView):
    model = FooterCopyright
    form_class = FooterCopyrightForm

class SEOSettingsView(BaseUpdateView):
    model = SEOSettings
    form_class = SEOSettingsForm


class PaymentMethodListView(ListView):
    model = PaymentMethod
    template_name = 'paymentmethod_list.html'
    context_object_name = 'payment_methods'

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

class PaymentMethodCreateView(CreateView):
    model = PaymentMethod
    form_class = PaymentMethodForm
    template_name = 'edit.html'
    success_url = reverse_lazy('paymentmethod-list')
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

class PaymentMethodUpdateView(UpdateView):
    model = PaymentMethod
    fmodel = PaymentMethod
    form_class = PaymentMethodForm
    template_name = 'edit.html'
    success_url = reverse_lazy('paymentmethod-list')
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

class PaymentMethodDeleteView(DeleteView):
    model = PaymentMethod
    success_url = reverse_lazy('paymentmethod-list')

class PaymentMethodToggleView(View):
    def post(self, request, pk):
        method = get_object_or_404(PaymentMethod, pk=pk)
        method.active = not method.active
        method.save()
        return redirect('paymentmethod-list')

# creating a base class for all api classes
class BaseApiView(ListAPIView):
    def get_queryset(self):
        return self.model.objects.all()


class LogoSettingsApiView(BaseApiView):
    model = LogoSettings
    serializer_class = LogoSettingsSerializer

class GeneralSettingsApiView(BaseApiView):
    queryset = GeneralSettings
    serializer_class = GeneralSettingsSerializer

class ColorSettingApiView(BaseApiView):
    model = ColorSettings
    serializer_class = ColorSettingsSerializer

class ContactSettingsApiView(BaseApiView):
    model = ContactSettings
    serializer_class = ContactSettingsSerializer

class CurrencySettingsApiView(BaseApiView):
    model = CurrencySettings
    serializer_class = CurrencySettingsSerializer

class HRMSettingsApiView(BaseApiView):
    model = HRMSettings
    serializer_class = HRMSettingsSerializer

class SMSSettingsApiView(BaseApiView):
    model = SMSSettings
    serializer_class = SMSSettingsSerializer

class SocialSettings(BaseApiView):
    model = SocialSettings
    serializer_class = SocialSettingsSerializer

class OtherSettingsApiView(BaseApiView):
    model = OtherSettings
    serializer_class = OtherSettingsSerializer

class FooterLayoutApiView(BaseApiView):
    model = FooterLayout
    serializer_class = FooterLayoutSerializer

class FooterToptApiView(BaseApiView):
    model = FooterTop
    serializer_class = FooterTopSerializer

class SocialLinksApiView(BaseApiView):
    model = SocialLinks
    serializer_class = SocialLinksSerializer

class SubscribeFormApiView(BaseApiView):
    model = SubscribeForm
    serializer_class = SubscribeFormSerializer

class FooterColumnApiView(BaseApiView):
    model = FooterColumn
    serializer_class = FooterColumnSerializer

class FooterBottomApiView(BaseApiView):
    model = FooterBottom
    serializer_class = FooterBottomSerializer

class FooterCopyrightApiView(BaseApiView):
    model = FooterCopyright
    serializer_class = FooterCopyrightSerializer

class SEOSettingsApiView(BaseApiView):
    model = SEOSettings
    serializer_class = SEOSettingsSerializer

class PaymentMethodApiView(BaseApiView):
    model = PaymentMethod
    serializer_class = PaymentMethodSerializer
