from django.urls import path
from .views import (ConversationListCreateAPIView, MessageCreateAPIView, ConversationDeleteAPIView)

urlpatterns = [
    path('api/chat/', ConversationListCreateAPIView.as_view(), name='conversation-list-create'),
    path('api/chat/<int:conversation_id>/', MessageCreateAPIView.as_view(), name='message-create'),
    path('api/chat/<int:conversation_id>/delete/', ConversationDeleteAPIView.as_view(), name='delete-conversation'),
]