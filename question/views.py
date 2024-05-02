from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import UserProfile
from .models import UserAnswer, Question
from .utils import generate_question_and_stories


class GenerateQuestionView(APIView):
    def post(self, request):
        num_stories = request.data.get('num_stories', 2)
        response_data = generate_question_and_stories(num_stories)
        return Response(response_data, status=status.HTTP_201_CREATED)


class SubmitQuestionAnswerView(APIView):
    def post(self, request):
        story_id = request.data.get('story_id')
        question_id = request.data.get('question_id')
        user_nickname = request.data.get('nickname')

        print("nickname is:", user_nickname)
        user = get_object_or_404(UserProfile, nickname=user_nickname)
        print("user 1 is:", user)
        user2 = UserProfile.objects.filter(nickname=user_nickname).first()
        print("user2 is:", user2)
        question = get_object_or_404(Question, pk=question_id)

        is_right_answer = story_id in question.non_synthetic_story_ids

        user_answer = UserAnswer.objects.create(
            user=user,
            question=question,
            non_synthetic_real_answer=story_id,
            user_answer=story_id,
            is_right_answer=is_right_answer
        )

        return Response(status=status.HTTP_201_CREATED)
