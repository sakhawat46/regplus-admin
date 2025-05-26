from django.contrib import admin
from .models import SurveyQuestion, SurveyOption

# Inline form for options inside the question form
class SurveyOptionInline(admin.TabularInline):
    model = SurveyOption
    extra = 4  # Show 4 blank options by default
    min_num = 1
    max_num = 10
    can_delete = True

# Main admin for SurveyQuestion
@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ['order', 'question_text']
    ordering = ['order']
    inlines = [SurveyOptionInline]
