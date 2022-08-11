# Register your models here.
from django.contrib import admin

from .models import UserEntry


class UserEntryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "collection",
        "won",
        "description",
    )



admin.site.register(UserEntry)