from django.db import models
import uuid
from profiles.models import UserProfile
from products.models import Collection


# Create your models here.
class UserEntry(models.Model):
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
        return f"{self.user_profile} raffle entry"


class Prize(models.Model):
    raffle_entry = models.OneToOneField(
        UserEntry, on_delete=models.SET_NULL, null=True
    )



    def _generate_coupon_number(self):
        """
        Generate a random, unique coupon number using UUID
        """
        return uuid.uuid4().hex.upper()

