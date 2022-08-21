"""raffle admin"""
from django.contrib import admin

from .models import UserEntry, Prize


class UserEntryAdmin(admin.ModelAdmin):
    """User Entry Admin"""
    list_display = (
        "user",
        "collection",
        "won",
        "description",
    )

class PrizeAdmin(admin.ModelAdmin):
    """Prize Admin"""
    list_display = (
        "raffle_entry",
        "coupon_code",
    )

admin.site.register(UserEntry)
admin.site.register(Prize)
