# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('Check/', list_models, name='Check'),
    path('api/chat/', ChatBotView.as_view(), name='chatbot'),
    path('api/chat/public/', PublicChatBotView.as_view(), name='public-chatbot'),
]