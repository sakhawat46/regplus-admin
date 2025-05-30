from rest_framework import serializers
from .models import MainModel,SurveyQuestion, SurveyOption




class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainModel
        fields=['id','title','files','description']
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainModel
        fields=['id','title','files']

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainModel
        fields=['id','title','description']



class HomeHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainModel
        fields=['id','title','files','subtitle','description']

class HomecardSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainModel
        fields=['id','title','files','description']

class HomeFooterUpperSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainModel
        fields=['id','title','subtitle','files']

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainModel
        fields=['id','title','description']


class SurveyOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyOption
        fields = ['id', 'option_text']


class SurveyQuestionSerializer(serializers.ModelSerializer):
    options = SurveyOptionSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyQuestion
        fields = ['id', 'question_text', 'order', 'options']