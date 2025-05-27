from rest_framework import serializers
from .models import MainModel




class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainModel
        fields=['id','title','files','description']