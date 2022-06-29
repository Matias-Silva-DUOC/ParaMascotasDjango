from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   = User
        fields  = ["email_usuario", "contra_usuario"]