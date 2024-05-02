from django.contrib.auth.models import User
from django.db import models

from django_better_admin_arrayfield.models.fields import ArrayField

from user.models import UserProfile


class Question(models.Model):
    question_content = models.TextField()
    synthetic_story_ids = ArrayField(models.IntegerField(), blank=True, null=True)
    non_synthetic_story_ids = ArrayField(models.IntegerField(), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserAnswer(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    non_synthetic_real_answer = models.IntegerField()
    user_answer = models.IntegerField()
    is_right_answer = models.BooleanField(default=Fagstlse)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
