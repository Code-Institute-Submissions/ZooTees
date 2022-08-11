from django.db import models
from profiles.models import UserProfile
from products.models import Collection


# Create your models here.
class UserEntry(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="raffle",
    )
    collection = models.ForeignKey(
        Collection, null=True, on_delete=models.SET_NULL
    )
    won = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.user_profile} raffle entry"
