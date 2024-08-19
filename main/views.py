from rest_framework import generics
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, RequestSerializer
from .models import User, Request


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Request(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
