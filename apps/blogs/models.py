from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

#Model for blgs category
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Enter Category')
    slug = models.SlugField(max_length=255, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
#model for blog
class Blog(models.Model):
    thumbnail = models.ImageField(upload_to='blog_images', verbose_name='Image', blank=False, null=False)
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', verbose_name="Select Category")
    author = models.CharField(max_length=100, verbose_name='Enter Author Name')
    description = RichTextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author