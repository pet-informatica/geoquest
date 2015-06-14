from django.shortcuts import render
import random

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from questions.models import Question, Category, Answer
from questions.serializers import QuestionSerializer, CategorySerializer, AnswerSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_fields = ('category',)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class RandomQuestion(APIView):
    
    queryset = Question.objects.all()
    
    def get(self, request, format=None):
        self.queryset = Question.objects.raw('SELECT * FROM questions_question Q WHERE Q.id NOT IN (SELECT A.question_id FROM questions_answer A WHERE A.answer=Q.correct_answer AND A.user_id=1) ORDER BY RANDOM()')
        serializer = QuestionSerializer(self.queryset, context={'request': request}, many=True)
        return Response(serializer.data)
        