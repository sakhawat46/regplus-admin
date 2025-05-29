# serializers.py
from rest_framework import serializers
from .models import *

class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['id', 'user', 'message', 'response', 'created_at']
        read_only_fields = ['user', 'response', 'created_at']
        
        




# class MessageSerializer(serializers.ModelSerializer):
#     sender = serializers.ReadOnlyField(source='sender.email')
#     class Meta:
#         model = Message
#         fields = ['id', 'sender', 'content', 'timestamp']

# class ChatSerializer(serializers.ModelSerializer):
#     messages = MessageSerializer(many=True, read_only=True)
#     class Meta:
#         model = Chat
#         fields = ['id', 'participants', 'messages']