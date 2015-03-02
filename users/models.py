from django.db import models
from django_facebook.models import FacebookModel

from questions.models import Badge

class CustomUser(FacebookModel):

    badges = models.ManyToManyField(Badge)
