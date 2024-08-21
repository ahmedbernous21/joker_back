from rest_framework import generics
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, RequestSerializer, StatisticsSerializer
from .models import User, Request
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Avg, Count, Sum


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


class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class StatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        if not start_date or not end_date:
            today = timezone.now().date()
            start_date = end_date = today

        requests = Request.objects.filter(
            creation_date__date__range=[start_date, end_date]
        )

        # Calculate statistics
        total_requests = requests.count()
        unseen_requests = requests.filter(state="unseen").count()
        pending_requests = requests.filter(state="pending").count()
        in_progress_requests = requests.filter(state="progress").count()
        finished_requests = requests.filter(state="finished").count()
        delivered_requests = requests.filter(is_delivered=True).count()

        conversion_rate = (
            (finished_requests + delivered_requests) / total_requests * 100
            if total_requests > 0
            else 0
        )

        total_revenue = (
            requests.filter(state="finished").aggregate(total_revenue=Sum("price"))[
                "total_revenue"
            ]
            or 0
        )

        repetitions_count = (
            requests.aggregate(Sum("repetitions"))["repetitions__sum"] or 0
        )

        top_article = (
            requests.values("article")
            .annotate(count=Count("article"))
            .order_by("-count")
            .first()
        )
        top_article = top_article["article"] if top_article else ""

        top_color = (
            requests.values("color")
            .annotate(count=Count("color"))
            .order_by("-count")
            .first()
        )
        top_color = top_color["color"] if top_color else ""

        data = {
            "total_requests": total_requests,
            "unseen_requests": unseen_requests,
            "pending_requests": pending_requests,
            "in_progress_requests": in_progress_requests,
            "finished_requests": finished_requests,
            "delivered_requests": delivered_requests,
            "conversion_rate": conversion_rate,
            "total_revenue": total_revenue,
            "repetitions_count": repetitions_count,
            "top_article": top_article,
            "top_color": top_color,
        }
        serializer = StatisticsSerializer(data)
        print("here", serializer)
        return Response(serializer.data)
