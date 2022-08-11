from django import forms
from .models import UserEntry


class UserEntryForm(forms.ModelForm):
    class Meta:
        model = UserEntry
        fields = "__all__"
        widgets = {
            "won": forms.HiddenInput(),
            "user_profile": forms.HiddenInput(),
        }
