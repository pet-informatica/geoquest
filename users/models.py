from django.db import models
from django_facebook.models import FacebookModel
from django.contrib.auth.models import AbstractUser, UserManager

from questions.models import Badge

class CustomUser(AbstractUser, FacebookModel):

    badges = models.ManyToManyField(Badge)