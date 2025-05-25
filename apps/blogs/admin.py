from django.contrib import admin
from .models import Category, Blog


#Register Category Models and auto slug field
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

#Register Blog Models and auto slug field
class BlogAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug': ('blog_title',)}
admin.site.register(Blog, BlogAdmin)