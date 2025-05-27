from django.urls import path
from .views import UserListView, UserCreateView, UserCreateSuccessView, UserUpdateView, UserDeleteView



urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/create/success/<int:pk>/', UserCreateSuccessView.as_view(), name='user_create_success'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', UserCreateSuccessView.as_view(), name='user-delete'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

]

