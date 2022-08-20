# Register your models here.
from django.contrib import admin

from .models import UserEntry, Prize


class UserEntryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "collection",
        "won",
        "description",
    )

class PrizeAdmin(admin.ModelAdmin):
    list_display = (
        "raffle_entry",
        "coupon_code",
    )

admin.site.register(UserEntry)
admin.site.register(Prize)
