from rest_framework import serializers

from django.conf import settings

from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email',)