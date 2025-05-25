from django import forms
from .models import Service
from django.core.exceptions import ValidationError

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'image', 'description', 'service_showing_order']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter service title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter service description',
                'rows': 4
            }),
            'service_showing_order': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter display order number'
            }),
        }
        labels = {
            'service_showing_order': 'Display Order',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })

    def clean_service_showing_order(self):
        order = self.cleaned_data.get('service_showing_order')
        if order < 0:
            raise ValidationError("Display order cannot be negative.")
        return order

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise ValidationError("Title must be at least 3 characters long.")
        return title
