from django.urls import path
from .views import CustomAdminCompanyInfo,CustomTermsAndCondition,CustomPrivacyPolicy,CustomFooterInfo

urlpatterns = [
    path('company-info/', CustomAdminCompanyInfo.as_view(), name='company_info'),
    path('terms-condition/', CustomTermsAndCondition.as_view(), name='terms_condition'),
    path('privacy-policy/', CustomPrivacyPolicy.as_view(), name='privacy_policy'),
    path('edit-footer/', CustomFooterInfo.as_view(), name='edit_footer'),
]
