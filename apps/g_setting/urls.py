from django.urls import path
from .views import CustomAdminCompanyInfo,CustomTermsAndCondition,CustomPrivacyPolicy,CustomFooterInfo,CompanyInfoListAPIView,TermsAndConditionsListAPIView,PrivacyPolicyListAPIView

urlpatterns = [
    path('company-info/', CustomAdminCompanyInfo.as_view(), name='company_info'),
    path('terms-condition/', CustomTermsAndCondition.as_view(), name='terms_condition'),
    path('privacy-policy/', CustomPrivacyPolicy.as_view(), name='privacy_policy'),
    path('edit-footer/', CustomFooterInfo.as_view(), name='edit_footer'),

    # apis
    path('api/company-info/', CompanyInfoListAPIView.as_view(), name='api_company_info'),
    path('api/terms-condition/', TermsAndConditionsListAPIView.as_view(), name='api_terms_condition'),
    path('api/privacy-policy/', PrivacyPolicyListAPIView.as_view(), name='api_privacy_policy'),
]
