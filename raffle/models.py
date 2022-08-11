from django.db import models
from django.contrib.auth.models import User
from products.models import Collection


# Create your models here.
class UserEntry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    collection = models.ForeignKey(
        Collection, null=True, blank=True, on_delete=models.SET_NULL
    )
    won = models.BooleanField(default=True)
    description = models.TextField()


    def __str__(self):
        return f"{self.user.username} raffle entry"
