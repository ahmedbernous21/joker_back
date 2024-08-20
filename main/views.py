from rest_framework import generics
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, RequestSerializer
from .models import User, Request


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user = authenticate(
            email=self.request.data.get("email"),
            password=self.request.data.get("password"),
        )
        if user and user.is_active:
            login(self.request, user)


class Request(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
