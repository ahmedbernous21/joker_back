from django.urls import path
from .views import UserList, RequestList, StatisticsView


urlpatterns = [
    path("api/users/", UserList.as_view(), name="users"),
    path("api/requests/", RequestList.as_view(), name="requests"),
    path("api/statistics/", StatisticsView.as_view(), name="statistics"),
]
