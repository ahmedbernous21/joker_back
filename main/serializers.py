# views.py
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from .models import User, Request


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["name"]


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = "__all__"
