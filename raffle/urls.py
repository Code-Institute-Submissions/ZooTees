from django.urls import path
from . import views

urlpatterns = [
    path("", views.raffle, name="raffle"),
]
