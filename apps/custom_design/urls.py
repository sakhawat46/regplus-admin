from django.urls import path
from .views import (
    SurveyQuestionListView,
    SurveyQuestionCreateView,
    SurveyQuestionUpdateView,
    SurveyQuestionDeleteView,
    survey_question_view, survey_result_view,CustomAdminAboutUsView,CustomAdminHeruSection
)

urlpatterns = [
    path('survey/', SurveyQuestionListView.as_view(), name='survey_admin_list'),
    path('survey/add/', SurveyQuestionCreateView.as_view(), name='survey_admin_add'),
    path('survey/<int:pk>/edit/', SurveyQuestionUpdateView.as_view(), name='survey_admin_edit'),
    path('survey/<int:pk>/delete/', SurveyQuestionDeleteView.as_view(), name='survey_admin_delete'),
    path('survey/question/<int:question_order>/', survey_question_view, name='survey_question'),
    path('survey/result/', survey_result_view, name='survey_result'),
     path('admin-dashboard/about-us/', CustomAdminAboutUsView.as_view(), name='custom_admin_about_us'),
     path('admin-dashboard/home-heru/', CustomAdminHeruSection.as_view(), name='custom_admin_about_us'),
]
