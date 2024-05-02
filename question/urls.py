from django.urls import path

from question.views import GenerateQuestionView, SubmitQuestionAnswerView

urlpatterns = [
    path('generate/', GenerateQuestionView.as_view(), name='generate-question'),
    path('answer/', SubmitQuestionAnswerView.as_view(), name='submit-answer')
]
