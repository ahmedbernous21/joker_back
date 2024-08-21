# views.py
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from .models import User, Request


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = "__all__"


class StatisticsSerializer(serializers.Serializer):
    total_requests = serializers.IntegerField()
    unseen_requests = serializers.IntegerField()
    pending_requests = serializers.IntegerField()
    in_progress_requests = serializers.IntegerField()
    finished_requests = serializers.IntegerField()
    delivered_requests = serializers.IntegerField()
    conversion_rate = serializers.FloatField()
    total_revenue = serializers.IntegerField()
    repetitions_count = serializers.IntegerField()
    top_article = serializers.CharField()
    top_color = serializers.CharField()
