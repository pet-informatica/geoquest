import json
from django.http import HttpResponse

from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets, generics
from questions.models import Answer, Question, Category
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserStatistics(APIView):

    queryset = Answer.objects.all()

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        user = request.user
        answers = Answer.objects.filter(user = user)
        result = {}
        for category in categories:
            result[category.name] = {
                'correct': 0, 
                'total': Question.objects.filter(category = category).count()
            }
            for answer in answers:
                if answer.question.category == category and answer.answer == answer.question.correct_answer:
                    result[category.name]['correct'] = result[category.name]['correct'] + 1         
        return HttpResponse(json.dumps(result), content_type='application/json')