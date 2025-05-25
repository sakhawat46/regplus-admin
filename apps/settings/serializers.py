from rest_framework import serializers
from .models import (
    LogoSettings, GeneralSettings, ColorSettings, ContactSettings,
    CurrencySettings, HRMSettings, SMSSettings, SocialSettings, OtherSettings,
    FooterLayout, FooterTop, SocialLinks, SubscribeForm,
    FooterColumn, FooterBottom, FooterCopyright, SEOSettings, PaymentMethod
)

class LogoSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoSettings
        fields = '__all__'

class GeneralSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSettings
        fields = '__all__'

class ColorSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorSettings
        fields = '__all__'

class ContactSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSettings
        fields = '__all__'

class CurrencySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencySettings
        fields = '__all__'

class HRMSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRMSettings
        fields = '__all__'

class SMSSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSSettings
        fields = '__all__'

class SocialSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialSettings
        fields = '__all__'

class OtherSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSettings
        fields = '__all__'

class FooterLayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLayout
        fields = '__all__'

class FooterTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterTop
        fields = '__all__'

class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = '__all__'

class SubscribeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeForm
        fields = '__all__'

class FooterColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterColumn
        fields = '__all__'

class FooterBottomSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterBottom
        fields = '__all__'

class FooterCopyrightSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterCopyright
        fields = '__all__'

class SEOSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOSettings
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
