from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import CompanyInfo, termsAlsoPrivacy

# Company Info Form
class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = [
            'company_name', 'company_email', 'company_phone',
            'company_address', 'company_logo',
            'facebook_link', 'twitter_link', 'instagram_link'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company_address': forms.Textarea(attrs={'class': 'form-control'}),
            'company_logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'facebook_link': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

# Base form for Terms/Privacy
class TermsPrivacyBaseForm(forms.ModelForm):
    class Meta:
        model = termsAlsoPrivacy
        fields = ['title', 'content', 'page_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditorWidget(attrs={'class': 'form-control'}),
            'page_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Terms and Conditions form
class TermsAndConditionsForm(TermsPrivacyBaseForm):
    pass

# Privacy Policy form
class PrivacyPolicyForm(TermsPrivacyBaseForm):
    pass




from .models import FooterInfo

class FooterInfoForm(forms.ModelForm):
    class Meta:
        model = FooterInfo
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_link': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin_link': forms.URLInput(attrs={'class': 'form-control'}),
            'copyright_text': forms.TextInput(attrs={'class': 'form-control'}),
        }
