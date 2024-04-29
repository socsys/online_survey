from django.contrib import admin
from .models import Question, UserAnswer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_content')
    # Add any other configurations you need

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'user_answer')
