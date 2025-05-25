# blog/forms.py
from django import forms
from .models import Category, Blog
from django.utils.text import slugify

# From for category
class CategoryForm(forms.ModelForm):
    slug = forms.CharField(required=False, label='Slug (Leave blank to set auto)')
    class Meta:
        model = Category
        fields = ['name', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter category name'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].widget.attrs.update({'disabled': 'disabled'})

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            # Auto-generate slug from name if slug is empty
            name = self.cleaned_data.get('name')
            slug = slugify(name)
        return slug

# From for Blog
class BlogForm(forms.ModelForm):
    slug = forms.CharField(required=False, label='Slug (Leave blank to set auto)')
    class Meta:
        model = Blog
        fields = ['thumbnail', 'blog_title', 'slug', 'category', 'author', 'description']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].widget.attrs.update({'disabled': 'disabled'})

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            # Auto-generate slug from name if slug is empty
            blog_title = self.cleaned_data.get('blog_title')
            slug = slugify(blog_title)
        return slug
