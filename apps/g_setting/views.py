from django.shortcuts import render,redirect

from .forms import CompanyInfoForm, TermsAndConditionsForm, PrivacyPolicyForm, FooterInfoForm
from .models import CompanyInfo,termsAlsoPrivacy, FooterInfo
from web_project import TemplateLayout
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.views import View
from .serializers import CompanyInfoSerializer,TermsAndConditinSerializer,PrivacyPolicySerializer
from rest_framework.response import Response
# Create your views here.


class CustomAdminCompanyInfo(View):
    template_name = 'info_com.html'

    def get(self, request):
        company_info, _ = CompanyInfo.objects.get_or_create(pk=1)
        form = CompanyInfoForm(instance=company_info)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        company_info, _ = CompanyInfo.objects.get_or_create(pk=1)
        form = CompanyInfoForm(request.POST, request.FILES, instance=company_info)
        context = self.get_context_data(form=form)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_about_us')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = kwargs
        context = TemplateLayout.init(self, context)
        return context
class CustomTermsAndCondition(View):
    template_name = 'terms.html'

    def get(self, request):
        term_condt, _ = termsAlsoPrivacy.objects.get_or_create(pk=1)
        form = TermsAndConditionsForm(instance=term_condt)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        term_condt, _ = termsAlsoPrivacy.objects.get_or_create(pk=1)
        form = TermsAndConditionsForm(request.POST, request.FILES, instance=term_condt)
        context = self.get_context_data(form=form)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_about_us')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = kwargs
        context = TemplateLayout.init(self, context)
        return context
class CustomPrivacyPolicy(View):
    template_name = 'policy.html'

    def get(self, request):
        privacy_info, created = termsAlsoPrivacy.objects.get_or_create(page_name='privacy')
        form = PrivacyPolicyForm(instance=privacy_info)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        privacy_info, created = termsAlsoPrivacy.objects.get_or_create(page_name='privacy')
        form = PrivacyPolicyForm(request.POST, request.FILES, instance=privacy_info)
        context = self.get_context_data(form=form)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_about_us')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = kwargs
        context = TemplateLayout.init(self, context)
        return context
    


class CustomFooterInfo(View):
    template_name = 'footer_edit.html'

    def get(self, request):
        footer, _ = FooterInfo.objects.get_or_create(pk=1)
        form = FooterInfoForm(instance=footer)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        footer, _ = FooterInfo.objects.get_or_create(pk=1)
        form = FooterInfoForm(request.POST, request.FILES, instance=footer)
        context = self.get_context_data(form=form)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_about_us')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = kwargs
        context = TemplateLayout.init(self, context)
        return context
    

class CompanyInfoListAPIView(APIView):
    """
    API view to list company information.
    """
    def get(self, request):
        company_info = CompanyInfo.objects.all()
        serializer = CompanyInfoSerializer(company_info, many=True)
        return Response(serializer.data)
    
class TermsAndConditionsListAPIView(APIView):
    """
    API view to list terms and conditions.
    """
    def get(self, request):
        terms_conditions = termsAlsoPrivacy.objects.filter(page_name='terms')
        serializer = TermsAndConditinSerializer(terms_conditions, many=True)
        return Response(serializer.data)
    
class PrivacyPolicyListAPIView(APIView):
    """
    API view to list privacy policy.
    """
    def get(self, request):
        privacy_policy = termsAlsoPrivacy.objects.filter(page_name='privacy')
        serializer = PrivacyPolicySerializer(privacy_policy, many=True)
        return Response(serializer.data)
