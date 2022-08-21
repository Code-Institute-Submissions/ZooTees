"""raffle urls"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.raffle, name="raffle"),
    path("login", views.raffle_login, name="raffle_login"),
]
