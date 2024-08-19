from django.contrib import admin
from .models import User, Request

# Register your models here.
admin.site.register(User)


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        "article",
        "phone",
        "size",
        "color",
        "creation_date",
        "is_seen",
        "is_delivered",
    )
    search_fields = ("article", "size", "is_delivered")
