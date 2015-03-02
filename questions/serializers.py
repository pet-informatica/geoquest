from rest_framework import serializers

from questions.models import Question, Category, Answer

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
