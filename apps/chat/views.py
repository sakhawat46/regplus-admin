from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
import google.generativeai as genai
from django.conf import settings

User = get_user_model()

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

class ConversationListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        conversations = Conversation.objects.filter(users=request.user)
        serializer = ConversationSerializer(conversations, many=True)

        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "Successfully retrieved",
            "data": serializer.data
        }
        return Response(response_data)


    def post(self, request):
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        serializer = ConversationSerializer(conversation)
        
        response_data = {
                "success": True,
                "status": status.HTTP_201_CREATED,
                "message": "Successfully created",
                "data": serializer.data
            }
        return Response(response_data, status=status.HTTP_201_CREATED)


    


class MessageCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, conversation_id):
        conversation = get_object_or_404(Conversation.objects.filter(users=request.user), pk=conversation_id)
        
        # Validate input data
        question = request.data.get('question')
        if not question:
            return Response({'error': 'Question field is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create message with empty answer initially
        message = Message.objects.create(conversation=conversation, sender=request.user, question=question, answer="")
        
        # Get response from Gemini
        try:
            response = model.generate_content(question)
            message.answer = response.text
            message.save()
        except Exception as e:
            message.answer = f"Error generating response: {str(e)}"
            message.save()
        
        # Serialize and return the message
        serializer = MessageSerializer(message)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        response_data = {
                "success": True,
                "status": status.HTTP_201_CREATED,
                "message": "Successfully created",
                "data": serializer.data
            }
        return Response(response_data, status=status.HTTP_201_CREATED)



class ConversationDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, conversation_id):
        try:
            conversation = Conversation.objects.get(id=conversation_id,users__id=request.user.id)
            conversation.delete()

            response_data = {
                    "success": True,
                    "status": status.HTTP_204_NO_CONTENT,
                    "message": "Conversation deleted successfully"
                }
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
                        
        except Conversation.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

