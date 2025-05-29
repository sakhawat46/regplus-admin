# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import ChatHistory
from .serializers import ChatHistorySerializer
import google.generativeai as genai
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

class ChatBotView(APIView):
    permission_classes = [IsAuthenticated]  # JWT will handle authentication
    
    def get(self, request):
        chats = ChatHistory.objects.filter(user=request.user).order_by('-created_at')[:20]
        serializer = ChatHistorySerializer(chats, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        message = request.data.get('message', '').strip()
        if not message:
            return Response({'error': 'Message cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Get response from Gemini
            response = model.generate_content(message)
            response_text = response.text
            
            # Save to database
            chat = ChatHistory.objects.create(
                user=request.user,
                message=message,
                response=response_text
            )
            
            serializer = ChatHistorySerializer(chat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PublicChatBotView(APIView):
    # No authentication required
    permission_classes = []
    
    def post(self, request):
        message = request.data.get('message', '').strip()
        if not message:
            return Response({'error': 'Message cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Get response from Gemini
            response = model.generate_content(message)
            response_text = response.text
            
            # Save to database (anonymous user)
            chat = ChatHistory.objects.create(
                message=message,
                response=response_text
            )
            
            serializer = ChatHistorySerializer(chat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        

@login_required
def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            # Get response from Gemini
            response = model.generate_content(message)
            
            # Save to database
            ChatHistory.objects.create(
                user=request.user,
                message=message,
                response=response.text
            )
    
    # Get last 10 chats
    chats = ChatHistory.objects.filter(user=request.user).order_by('-created_at')[:10]
    return render(request, 'chat.html', {'chats': chats})


#Check Availavle Model
def list_models(request):
    models = genai.list_models()
    for m in models:
        print(m.name)
    return HttpResponse("Check console for available models")



# from rest_framework import generics
# from .models import Chat, Message
# from .serializers import ChatSerializer, MessageSerializer

# class ChatListView(generics.ListAPIView):
#     serializer_class = ChatSerializer
#     def get_queryset(self):
#         user = self.request.user
#         return Chat.objects.filter(participants=user)

# class MessageListView(generics.ListAPIView):
#     serializer_class = MessageSerializer
#     def get_queryset(self):
#         chat_id = self.kwargs['chat_id']
#         return Message.objects.filter(chat_id=chat_id)