from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from user.models import UserProfile
from .models import UserAnswer, Question
from .utils import generate_question_and_stories


@method_decorator(csrf_exempt, name='dispatch')
class GenerateQuestionView(APIView):
    def post(self, request):
        num_stories = request.data.get('num_stories', 2)
        response_data = generate_question_and_stories(num_stories)
        return Response(response_data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class SubmitQuestionAnswerView(APIView):
    def post(self, request):
        story_id = request.data.get('story_id')
        question_id = request.data.get('question_id')
        user_nickname = request.data.get('nickname')

        user = get_object_or_404(UserProfile, nickname=user_nickname)
        question = get_object_or_404(Question, pk=question_id)

        is_right_answer = True if int(story_id) == question.non_synthetic_story_ids[0] else False

        user_answer = UserAnswer.objects.create(
            user=user,
            question=question,
            non_synthetic_real_answer=question.non_synthetic_story_ids[0],
            user_answer=story_id,
            is_right_answer=is_right_answer
        )

        return Response(status=status.HTTP_201_CREATED)
