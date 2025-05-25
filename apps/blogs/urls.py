from django.urls import path
from .views import *

urlpatterns = [
    # Category URLs
    path('blog/categories/', CategoryListView.as_view(), name='category-list'),
    path('blog/categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('blog/categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('blog/categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # Blog URLs
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blog/add/', BlogCreateView.as_view(), name='blog-add'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog-edit'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
]