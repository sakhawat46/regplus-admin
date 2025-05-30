from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.




class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_phone = models.CharField(max_length=20, blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
     

    

    def __str__(self):
        return self.company_name if self.company_name else "Company Info"
    

class termsAlsoPrivacy(models.Model):
    title=models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    page_name=models.CharField(max_length=50, blank=True, null=True)



class FooterInfo(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    copyright_text = models.CharField(
        max_length=255,
        default="© 2025 Your Company. All rights reserved.",
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Footer Info - {self.company_name or 'Default'}"
