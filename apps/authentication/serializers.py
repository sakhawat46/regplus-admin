from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
User= get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'user_type', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email_or_username = data.get('email_or_username')
        password = data.get('password')

        user = authenticate(email=email_or_username, password=password)

        if user is None:
            user = authenticate(username=email_or_username, password=password)

        if user and user.is_active:
            return user
        raise serializers.ValidationError('Invalid credentials')
