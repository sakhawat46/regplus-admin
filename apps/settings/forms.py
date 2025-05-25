from django import forms
import json
from .models import (
    LogoSettings, GeneralSettings, ColorSettings, ContactSettings,
    CurrencySettings, HRMSettings, SMSSettings, SocialSettings, OtherSettings,
    FooterLayout, FooterTop, SocialLinks, SubscribeForm, FooterColumn,
    FooterBottom, FooterCopyright, SEOSettings, PaymentMethod
)

class BaseSettingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply common attributes to all fields
        for field_name, field in self.fields.items():
            # Add form-control class to all fields except checkboxes and radios
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'id': f'id_{field_name}'
                })

            # Special handling for different field types
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({
                    'class': 'form-check-input',
                    'id': f'id_{field_name}'
                })

            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'rows': 3,
                    'class': 'form-control'
                })

            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({
                    'class': 'form-control form-control-lg',
                    'accept': 'image/*'  # For image fields
                })

class LogoSettingsForm(BaseSettingsForm):
    class Meta:
        model = LogoSettings
        fields = '__all__'
        widgets = {
            'logo_light': forms.FileInput(attrs={
                'class': 'form-control form-control-lg',
                'accept': 'image/*',
                'data-preview': 'logo_light-preview'
            }),
            'logo_dark': forms.FileInput(attrs={
                'class': 'form-control form-control-lg',
                'accept': 'image/*',
                'data-preview': 'logo_dark-preview'
            }),
            'favicon': forms.FileInput(attrs={
                'class': 'form-control form-control-lg',
                'accept': 'image/x-icon,image/vnd.microsoft.icon',
                'data-preview': 'favicon-preview'
            }),
            'invoice_logo': forms.FileInput(attrs={
                'class': 'form-control form-control-lg',
                'accept': 'image/*',
                'data-preview': 'invoice_logo-preview'
            }),
        }

class GeneralSettingsForm(BaseSettingsForm):
    class Meta:
        model = GeneralSettings
        fields = '__all__'
        widgets = {
            'application_name': forms.TextInput(attrs={
                'placeholder': 'Enter application name',
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Enter author name',
            }),
            'default_menu': forms.CheckboxInput(attrs={
                'data-toggle': 'toggle',
                'data-on': 'Enabled',
                'data-off': 'Disabled',
            }),
            'search_feature': forms.CheckboxInput(attrs={
                'data-toggle': 'toggle',
                'data-on': 'Enabled',
                'data-off': 'Disabled',

            }),
        }

class ColorSettingsForm(BaseSettingsForm):
    class Meta:
        model = ColorSettings
        fields = '__all__'
        widgets = {
            'primary_color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control form-control-color',
                'style': 'width: 80px; height: 45px;'
            }),
            'primary_hover_link_color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control form-control-color',
                'style': 'width: 80px; height: 45px;'
            }),
            'whatsapp_button_shed_color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control form-control-color',
                'style': 'width: 80px; height: 45px;'
            }),
        }

class ContactSettingsForm(BaseSettingsForm):
    class Meta:
        model = ContactSettings
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@domain.com',
            }),
            'phone_whatsapp': forms.TextInput(attrs={
                'placeholder': '+1234567890',
            }),
            'price_range': forms.TextInput(attrs={
                'placeholder': 'e.g. $10 - $100',
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Street address',
            }),
        }

class CurrencySettingsForm(BaseSettingsForm):
    class Meta:
        model = CurrencySettings
        fields = '__all__'
        widgets = {
            'currency_symbul': forms.TextInput(attrs={
                'style': 'max-width: 80px;',
                'placeholder': '$'
            }),
        }

class HRMSettingsForm(BaseSettingsForm):
    class Meta:
        model = HRMSettings
        fields = '__all__'
        widgets = {
            'clock_in_max_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control timepicker',
                    'step': '900'  # 15 minute intervals
                },
                format='%H:%M'
            ),
            'clock_out_min_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control timepicker',
                    'step': '900'  # 15 minute intervals
                },
                format='%H:%M'
            ),
        }

class SMSSettingsForm(BaseSettingsForm):
    class Meta:
        model = SMSSettings
        fields = '__all__'
        widgets = {
            'twilio_sid': forms.PasswordInput(render_value=True, attrs={
                'placeholder': 'Enter Twilio SID',
            }),
            'auth_token': forms.PasswordInput(render_value=True, attrs={
                'placeholder': 'Enter Auth Token',
            }),
        }

class SocialSettingsForm(BaseSettingsForm):
    class Meta:
        model = SocialSettings
        fields = '__all__'
        widgets = {
            'google_analytics_code': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Paste Google Analytics code here',
            }),
            'facebook_pixel_code': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Paste Facebook Pixel code here',
            }),
            'facebook_chat_code': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Paste Facebook Chat code here',
            }),
        }

class OtherSettingsForm(BaseSettingsForm):
    class Meta:
        model = OtherSettings
        fields = '__all__'
        widgets = {
            'custom_css': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control code-editor',
                'data-mode': 'css',
                'placeholder': 'Enter your custom CSS here',
            }),
            'custom_js': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control code-editor',
                'data-mode': 'javascript',
                'placeholder': 'Enter your custom JavaScript here',
            }),
        }

class FooterLayoutForm(BaseSettingsForm):
    class Meta:
        model = FooterLayout
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter footer layout name',
            }),
        }

class FooterTopForm(BaseSettingsForm):
    class Meta:
        model = FooterTop
        fields = '__all__'
        widgets = {
            'subtitle': forms.TextInput(attrs={
                'placeholder': 'Enter subtitle text',
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter main title',
            }),
            'button_text': forms.TextInput(attrs={
                'placeholder': 'Enter button text',
            }),
            'button_url': forms.URLInput(attrs={
                'placeholder': 'https://example.com',
            }),
        }

class SocialLinksForm(BaseSettingsForm):
    class Meta:
        model = SocialLinks
        fields = '__all__'
        widgets = {
            'facebook': forms.URLInput(attrs={
                'placeholder': 'https://facebook.com/yourpage',
            }),
            'instagram': forms.URLInput(attrs={
                'placeholder': 'https://instagram.com/yourpage',
            }),
            'twitter': forms.URLInput(attrs={
                'placeholder': 'https://twitter.com/yourpage',
            }),
            'linkedin': forms.URLInput(attrs={
                'placeholder': 'https://linkedin.com/yourpage',
            }),
            'youtube': forms.URLInput(attrs={
                'placeholder': 'https://youtube.com/yourpage',
            }),
            'pinterest': forms.URLInput(attrs={
                'placeholder': 'https://pinterest.com/yourpage',
            }),
        }

class SubscribeFormForm(BaseSettingsForm):
    class Meta:
        model = SubscribeForm
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter subscription form title',
            }),
            'placeholder': forms.TextInput(attrs={
                'placeholder': 'Enter input placeholder text',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter description text',
                'rows': 3,
            }),
            'button_text': forms.TextInput(attrs={
                'placeholder': 'Enter button text',
            }),
        }

class FooterColumnForm(BaseSettingsForm):
    class Meta:
        model = FooterColumn
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter column title',
            }),
            'content_choice': forms.TextInput(attrs={
                'placeholder': 'Optional dropdown value',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control rich-text-editor',
                'placeholder': 'Enter column content (use <ul> and <li> tags for lists)',
            }),
        }

class FooterBottomForm(BaseSettingsForm):
    class Meta:
        model = FooterBottom
        fields = '__all__'
        widgets = {
            'small_text': forms.Textarea(attrs={
                'placeholder': 'Enter small text to appear under logo',
                'rows': 2,
            }),
            'first_column_title': forms.TextInput(attrs={
                'placeholder': 'Enter first column title',
            }),
            'first_column_choice': forms.TextInput(attrs={
                'placeholder': 'Enter first column choice',
            }),
            'first_column_description': forms.Textarea(attrs={
                'class': 'form-control rich-text-editor',
                'placeholder': 'Enter first column content',
            }),
            'second_column_title': forms.TextInput(attrs={
                'placeholder': 'Enter second column title',
            }),
            'second_column_description': forms.Textarea(attrs={
                'class': 'form-control rich-text-editor',
                'placeholder': 'Enter second column content',
            }),
            'third_column_title': forms.TextInput(attrs={
                'placeholder': 'Enter third column title',
            }),
            'third_column_description': forms.Textarea(attrs={
                'class': 'form-control rich-text-editor',
                'placeholder': 'Enter third column content',
            }),
        }

class FooterCopyrightForm(BaseSettingsForm):
    class Meta:
        model = FooterCopyright
        fields = '__all__'
        widgets = {
            'copyright_text': forms.TextInput(attrs={
                'placeholder': '© 2023 Your Company. All rights reserved.',
            }),
            'privacy_policy': forms.TextInput(attrs={
                'placeholder': 'Privacy Policy',
            }),
            'terms_page': forms.TextInput(attrs={
                'placeholder': 'Terms of Service',
            }),
        }

class SEOSettingsForm(BaseSettingsForm):
    class Meta:
        model = SEOSettings
        fields = '__all__'
        widgets = {
            'meta_title': forms.TextInput(attrs={
                'placeholder': 'Enter meta title (50-60 characters recommended)',
                'maxlength': '150',
            }),
            'tag_line': forms.TextInput(attrs={
                'placeholder': 'Enter short tag line for the site',
                'maxlength': '150',
            }),
            'meta_description': forms.Textarea(attrs={
                'placeholder': 'Enter meta description (150-160 characters recommended)',
                'rows': 3,
            }),
            'seo_keywords': forms.Textarea(attrs={
                'placeholder': 'Enter comma-separated keywords (e.g., keyword1, keyword2, keyword3)',
                'rows': 3,
                'help_text': 'Comma-separated keywords for SEO',
            }),
            'meta_image': forms.FileInput(attrs={
                'class': 'form-control form-control-lg',
                'accept': 'image/*',
                'data-preview': 'meta_image-preview'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['meta_title'].help_text = 'Recommended length: 50-60 characters'
        self.fields['meta_description'].help_text = 'Recommended length: 150-160 characters'
        self.fields['seo_keywords'].help_text = 'Comma-separated list of keywords (e.g., keyword1, keyword2)'


class PaymentMethodForm(BaseSettingsForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        widgets = {
            'name': forms.Select(attrs={
                'class': 'form-select',
                'data-control': 'select2',
                'data-placeholder': 'Select payment gateway'
            }),
            'config': forms.Textarea(attrs={
                'class': 'form-control json-editor',
                'rows': 8,
                'placeholder': '{\n  "api_key": "your_api_key",\n  "secret_key": "your_secret_key"\n}'
            }),
            'sandbox': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'data-toggle': 'toggle',
                'data-on': 'Sandbox Mode',
                'data-off': 'Live Mode',
                'data-onstyle': 'warning',
                'data-offstyle': 'success'
            }),
            'active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'data-toggle': 'toggle',
                'data-on': 'Active',
                'data-off': 'Inactive',
                'data-onstyle': 'success',
                'data-offstyle': 'danger'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add JSON validation help text
        self.fields['config'].help_text = 'Enter valid JSON configuration (e.g., {"api_key": "your_key", "secret": "your_secret"})'

    
