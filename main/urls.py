from django.urls import path
from .views import UserList, RequestList


urlpatterns = [
    path("api/users/", UserList.as_view(), name="users"),
    path("api/requests/", RequestList.as_view(), name="requests"),
]
