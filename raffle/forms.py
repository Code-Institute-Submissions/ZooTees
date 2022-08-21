"""raffle Forms"""
from django import forms
from .models import UserEntry


class UserEntryForm(forms.ModelForm):
    """ User Entry Form Models"""
    class Meta:
        model = UserEntry
        fields = "__all__"
        widgets = {
            "user_profile": forms.HiddenInput(),
        }
