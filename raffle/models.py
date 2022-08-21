"""raffle models"""
from django.db import models
from profiles.models import UserProfile
from products.models import Collection


# Create your models here.
class UserEntry(models.Model):
    """User Entry Model"""
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="raffle",
    )
    collection = models.ForeignKey(
        Collection, null=True, on_delete=models.SET_NULL
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.user_profile}'s raffle entry"


class Prize(models.Model):
    """Prize Model"""
    raffle_entry = models.OneToOneField(
        UserEntry,
        on_delete=models.SET_NULL,
        null=True,
    )
    coupon_code = models.CharField(max_length=32, null=True, editable=False)

    def __str__(self):
        return f"{self.raffle_entry.user_profile}'s prize"