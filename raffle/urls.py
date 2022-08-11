from django.urls import path
from . import views

urlpatterns = [
    path("", views.raffle_entry, name="raffle_entry"),
]
