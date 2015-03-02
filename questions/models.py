from django.db import models
from django.contrib.auth.models import User

ANSWER_CHOICES = (
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),
	('D', 'D'),
	('E', 'E'),
)

class Category(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=100)
    description = models.CharField(verbose_name="Descricao", max_length=200, blank=True)

class Question(models.Model):

    category = models.ForeignKey(Category)

    question = models.TextField(verbose_name='Pergunta')

    exam = models.CharField(verbose_name="Prova", max_length=100)

    option_a = models.CharField(verbose_name='Letra A', max_length=500)
    option_b = models.CharField(verbose_name='Letra B', max_length=500)
    option_c = models.CharField(verbose_name='Letra C', max_length=500)
    option_d = models.CharField(verbose_name='Letra D', max_length=500)
    option_e = models.CharField(verbose_name='Letra E', max_length=500)

    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)


class Answer(models.Model):

    user = models.ForeignKey(User)

    question = models.ForeignKey(Question)

    answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)

    date = models.DateTimeField(auto_now_add=True)
