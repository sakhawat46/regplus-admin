# from django.db import models

# # Create your models here.



# class MainModel(models.Model):
#     title=models.CharField(max_length=200)
#     files=models.FileField()
#     subtitle=models.CharField(max_length=200)
#     description=models.TextField()
#     page_section=models.CharField(max_length=50)
#     page_name=models.CharField(max_length=50)

#     def __str__(self):
#         return self.title
    

from django.db import models
from ckeditor.fields import RichTextField
PAGE_CHOICES = [
    ('home', 'Home'),
    ('about', 'About'),
    ('survey', 'Survey'),
    ('train&FAQ', 'Train&FAQ'),

]

SECTION_CHOICES = [
    ('hero', 'Hero'),
    ('middle','moddle'),
    ('card','card'),
    ('intro', 'Introduction'),
    ('down', 'Down'),
    
]

class MainModel(models.Model):
    title = models.CharField(max_length=200)
    files = models.FileField(upload_to='uploads/', blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    page_section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    page_name = models.CharField(max_length=50, choices=PAGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    class Meta:
        ordering = ['-created_at']  # Order by creation date, newest first

    def __str__(self):
        return f"{self.page_name} - {self.page_section}: {self.title}"




class SurveyQuestion(models.Model):
    question_text = RichTextField()
    order = models.PositiveIntegerField(default=0)  # To control question order

    def __str__(self):
        return f"Q{self.order}: {self.question_text[:50]}"


class SurveyOption(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text
