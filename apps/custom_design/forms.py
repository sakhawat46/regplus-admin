from django import forms
from .models import SurveyQuestion, SurveyOption,MainModel
from django.forms.models import inlineformset_factory
from ckeditor.widgets import CKEditorWidget
class SurveyQuestionForm(forms.ModelForm):
    class Meta:
        model = SurveyQuestion
        fields = ['question_text', 'order']

SurveyOptionFormSet = inlineformset_factory(
    SurveyQuestion,
    SurveyOption,
    fields=('option_text',),
    extra=4,
    can_delete=True,
    widgets = {
            'description': CKEditorWidget(),
        },
)


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = ['title', 'files', 'subtitle', 'description','page_section','page_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'page_section': forms.Select(attrs={'class': 'form-control'}),
            'page_name': forms.Select(attrs={'class': 'form-control'}),
            'description': CKEditorWidget(),
        }



class HeruSectionForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields=['title', 'files','subtitle','description', 'page_section','page_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'page_section': forms.Select(attrs={'class': 'form-control'}),
            'page_name': forms.Select(attrs={'class': 'form-control'}),
            'description': CKEditorWidget(),
        
        }


# forms.py
from django import forms
from .models import MainModel

class CardForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = ['title', 'files', 'description','page_section','page_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'page_section': forms.Select(attrs={'class': 'form-control'}),
            'page_name': forms.Select(attrs={'class': 'form-control'}),
            'description': CKEditorWidget(),
        }

class FooterUpperSectionForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields=['title', 'files', 'subtitle', 'page_section','page_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'page_section': forms.Select(attrs={'class': 'form-control'}),
            'page_name': forms.Select(attrs={'class': 'form-control'}),
        }

class TrainVideoForm(forms.ModelForm):
    class Meta:
        model=MainModel
        fields=['title','files','page_section','page_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'page_section': forms.Select(attrs={'class': 'form-control'}),
            'page_name': forms.Select(attrs={'class': 'form-control'}),
        }





class FAQForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = ['title', 'description', 'page_section', 'page_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': CKEditorWidget(),
            'page_section': forms.Select(attrs={'class': 'form-control'}),
            'page_name': forms.Select(attrs={'class': 'form-control'}),
        }