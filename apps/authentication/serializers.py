from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from apps.users.models import Profile
User= get_user_model()


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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'name', 'family_name', 'company_name', 'job_title']
        extra_kwargs = {
            'name': {'required': False},
            'family_name': {'required': False},
            'company_name': {'required': False},
            'avatar': {'required': False, 'allow_null': True},
        }

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        min_length=8,
        error_messages={
            'min_length': 'Password must be at least 8 characters long.'
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'password2', 'user_type', 'is_active', 'is_staff', 'created_at', 'profile']
        read_only_fields = ['id', 'created_at', 'user_type', 'is_active', 'is_staff',]
        extra_kwargs = {
            'email': {'required': True},
            'user_type': {'required': True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        if data['password'] != data.pop('password2'):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data



    def create(self, validated_data):
        # Get profile data or default to empty dict if none provided
        profile_data = validated_data.pop('profile', {})  

        # Create the user
        user = User.objects.create_user(
        email=validated_data['email'],
        password=validated_data['password'],
        user_type=validated_data.get('user_type', 'user'),
        is_active=validated_data.get('is_active', True),
        is_staff=validated_data.get('is_staff', False)
        )

        # Always create a profile (with provided data or defaults)
        Profile.objects.create(
        user=user,
        avatar=profile_data.get('avatar'),
        name=profile_data.get('name'),
        family_name=profile_data.get('family_name'),
        company_name=profile_data.get('company_name'),
        job_title=profile_data.get('job_title')
        )

        return user


    

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})  # Default to empty dict
        
        # Update user fields
        instance.email = validated_data.get('email', instance.email)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        instance.save()

        # Update profile
        if hasattr(instance, 'profile'):
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        elif profile_data:  # Create profile if it doesn't exist
            Profile.objects.create(user=instance, **profile_data)

        return instance
