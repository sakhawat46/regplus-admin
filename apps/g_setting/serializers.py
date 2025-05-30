from rest_framework import serializers

from .models import termsAlsoPrivacy, CompanyInfo

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class TermsAndConditinSerializer(serializers.ModelSerializer):
    class Meta:
        model=termsAlsoPrivacy
        fields = '__all__'
class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model=termsAlsoPrivacy
        fields = '__all__'

