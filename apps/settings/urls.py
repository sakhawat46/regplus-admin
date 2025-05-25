from django.urls import path
from .views import (
    LogoSettingsView, GeneralSettingsView, ColorSettingsView,
    ContactSettingsView, CurrencySettingsView, HRMSettingsView,
    SMSSettingsView, SocialSettingsView,OtherSettingsView,
    SettingsDashboardView, HeaderFooterDashboardView, FooterLayoutView,
    FooterTopView, SocialLinksView, SubscribeFormView,
    FooterColumnView, FooterBottomView, FooterCopyrightView,
    SEOSettingsView, PaymentMethodListView, PaymentMethodCreateView,
    PaymentMethodUpdateView, PaymentMethodDeleteView, PaymentMethodToggleView,

    # api view
    LogoSettingsApiView, GeneralSettingsApiView, ColorSettingApiView,
    ContactSettingsApiView, CurrencySettingsApiView, HRMSettingsApiView,
    SMSSettingsApiView, SocialSettings, OtherSettingsApiView,
    FooterLayoutApiView, FooterToptApiView, SocialLinksApiView,
    SubscribeFormApiView, FooterColumnApiView, FooterBottomApiView,
    FooterCopyrightApiView, SEOSettingsApiView, PaymentMethodApiView
)



urlpatterns = [
    path('settings/system-settings', SettingsDashboardView.as_view(), name='settings_dashboard'),
    path('settings/system-settings/logo', LogoSettingsView.as_view(), name='logo_settings'),
    path('settings/system-settings/general', GeneralSettingsView.as_view(), name='general_settings'),
    path('settings/system-settings/colors', ColorSettingsView.as_view(), name='color_settings'),
    path('settings/system-settings/contact', ContactSettingsView.as_view(), name='contact_settings'),
    path('settings/system-settings/currency', CurrencySettingsView.as_view(), name='currency_settings'),
    path('settings/system-settings/hrm', HRMSettingsView.as_view(), name='hrm_settings'),
    path('settings/system-settings/sms', SMSSettingsView.as_view(), name='sms_settings'),
    path('settings/system-settings/social', SocialSettingsView.as_view(), name='social_settings'),
    path('settings/system-settings/other', OtherSettingsView.as_view(), name='other_settings'),

    path('settings/header-footer', HeaderFooterDashboardView.as_view(), name='header_footer_dashboard'),
    path('settings/header-footer/footer-layout', FooterLayoutView.as_view(), name='footer_layout'),
    path('settings/header-footer/footer-top', FooterTopView.as_view(), name='footer_top'),
    path('settings/header-footer/footer-social-links', SocialLinksView.as_view(), name='footer_social_licks'),
    path('settings/header-footer/footer-subscribe-form', SubscribeFormView.as_view(), name='footer_subscribe_form'),
    path('settings/header-footer/footer-column', FooterColumnView.as_view(), name='footer_column'),
    path('settings/header-footer/footer-bottom', FooterBottomView.as_view(), name='footer_bottom'),
    path('settings/header-footer/footer-copyrights', FooterCopyrightView.as_view(), name='footer_copyrights'),

    path('settings/seo', SEOSettingsView.as_view(), name='seo'),

    path('settings/payment-method', PaymentMethodListView.as_view(), name='paymentmethod-list'),
    path('settings/payment-method/add', PaymentMethodCreateView.as_view(), name='add_payment_method'),
    path('settings/payment-method/<int:pk>/edit', PaymentMethodUpdateView.as_view(), name='update_payment_method'),
    path('settings/payment-method/<int:pk>/delete', PaymentMethodDeleteView.as_view(), name='delete_payment_method'),
    path('settings/payment-method/<int:pk>/toggle', PaymentMethodToggleView.as_view(), name='toggle_payment_method'),

    # Settings URLs
    path('api/settings/logo/', LogoSettingsApiView.as_view(), name='logo-settings-api'),
    path('api/settings/general/', GeneralSettingsApiView.as_view(), name='general-settings-api'),
    path('api/settings/color/', ColorSettingApiView.as_view(), name='color-settings-api'),
    path('api/settings/contact/', ContactSettingsApiView.as_view(), name='contact-settings-api'),
    path('api/settings/currency/', CurrencySettingsApiView.as_view(), name='currency-settings-api'),
    path('api/settings/hrm/', HRMSettingsApiView.as_view(), name='hrm-settings-api'),
    path('api/settings/sms/', SMSSettingsApiView.as_view(), name='sms-settings-api'),
    path('api/settings/social/', SocialSettings.as_view(), name='social-settings-api'),
    path('api/settings/other/', OtherSettingsApiView.as_view(), name='other-settings-api'),

    # Footer URLs
    path('api/footer/layout/', FooterLayoutApiView.as_view(), name='footer-layout-api'),
    path('api/footer/top/', FooterToptApiView.as_view(), name='footer-top-api'),
    path('api/footer/social-links/', SocialLinksApiView.as_view(), name='social-links-api'),
    path('api/footer/subscribe/', SubscribeFormApiView.as_view(), name='subscribe-form-api'),
    path('api/footer/column/', FooterColumnApiView.as_view(), name='footer-column-api'),
    path('api/footer/bottom/', FooterBottomApiView.as_view(), name='footer-bottom-api'),
    path('api/footer/copyright/', FooterCopyrightApiView.as_view(), name='footer-copyright-api'),

    # SEO URL
    path('api/settings/seo/', SEOSettingsApiView.as_view(), name='seo-settings-api'),

    # Payment URL
    path('api/payment-methods/', PaymentMethodApiView.as_view(), name='payment-methods-api'),
]
