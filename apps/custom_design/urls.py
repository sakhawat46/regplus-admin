from django.urls import path
from .views import (
    SurveyQuestionListView,
    SurveyQuestionCreateView,
    SurveyQuestionUpdateView,
    SurveyQuestionDeleteView,
    TrainVideoListView,
    TrainVideoCreateView,
    TrainVideoUpdateView,
    TrainVideoDeleteView,
    FAQListView, FAQCreateView, FAQUpdateView, FAQDeleteView,
    VideoViewApi,FaqViewApi,HomeHeroViewApi,HomecardViewApi,HomeFooterUpperSerializer,AboutUsViewApi,SurveyQuestionListApiView,
    survey_question_view, survey_result_view,CustomAdminAboutUsView,CustomAdminHeruSection,CardListView,CardCreateView,CardUpdateView,CardDeleteView,CardViewApi,CustomAdminFooterUpeer
)

urlpatterns = [
    path('survey/', SurveyQuestionListView.as_view(), name='survey_admin_list'),
    path('survey/add/', SurveyQuestionCreateView.as_view(), name='survey_admin_add'),
    path('survey/<int:pk>/edit/', SurveyQuestionUpdateView.as_view(), name='survey_admin_edit'),
    path('survey/<int:pk>/delete/', SurveyQuestionDeleteView.as_view(), name='survey_admin_delete'),
    path('survey/question/<int:question_order>/', survey_question_view, name='survey_question'),
    path('survey/result/', survey_result_view, name='survey_result'),
    path('admin-dashboard/about-us/', CustomAdminAboutUsView.as_view(), name='custom_admin_about_us'),
    path('admin-dashboard/home-heru/', CustomAdminHeruSection.as_view(), name='custom_hero_section'),
    path('admin-dashboard/home-footer/', CustomAdminFooterUpeer.as_view(), name='custom_admin_footer_upper'),
    #  path('admin-dashboard/faq-train/', TrainVideoSection.as_view(), name='train_section'),

    #cards edit
    path('cards/', CardListView.as_view(), name='manage_cards'),
    path('cards/add/', CardCreateView.as_view(), name='add_card'),
    path('cards/edit/<int:pk>/', CardUpdateView.as_view(), name='edit_card'),
    path('cards/delete/<int:pk>/', CardDeleteView.as_view(), name='delete_card'),


    #video section
    path('train-videos/', TrainVideoListView.as_view(), name='train_video_list'),
    path('train-videos/add/', TrainVideoCreateView.as_view(), name='train_video_add'),
    path('train-videos/<int:pk>/edit/', TrainVideoUpdateView.as_view(), name='train_video_edit'),
    path('train-videos/<int:pk>/delete/', TrainVideoDeleteView.as_view(), name='train_video_delete'),


    # faq question section
    path('faqs/', FAQListView.as_view(), name='faq_list'),
    path('faqs/add/', FAQCreateView.as_view(), name='faq_add'),
    path('faqs/<int:pk>/edit/', FAQUpdateView.as_view(), name='faq_edit'),
    path('faqs/<int:pk>/delete/', FAQDeleteView.as_view(), name='faq_delete'),


    # apis
    path('api/cards/', CardViewApi.as_view(), name='api_cards'),
    path('api/videos/', VideoViewApi.as_view(), name='api_videos'),
    path('api/faqs/', FaqViewApi.as_view(), name='api_faqs'),

    path('api/home-heru/', HomeHeroViewApi.as_view(), name='home_heru'),
    path('api/home-cards/', HomecardViewApi.as_view(), name='home_cards'),
    
    path('api/home-footer-upper/', HomeFooterUpperSerializer.as_view(), name='home_footer_upper'),
    path('api/about-us/',AboutUsViewApi.as_view(),name='about_us'),
    path('api/survey/questions/', SurveyQuestionListApiView.as_view(), name='survey-questions'),
]
