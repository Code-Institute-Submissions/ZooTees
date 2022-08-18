from django.shortcuts import render, redirect
from django.contrib import messages
from profiles.models import UserProfile
from raffle.models import UserEntry
from .forms import UserEntryForm


# Create your views here.
def raffle(request):
    """Add a raffle entry"""
    user_profile = UserProfile.objects.get(user=request.user)
    user_entry = UserEntry.objects.get(user_profile = user_profile)
    if user_entry:
        context = {
            "raffle_user": user_entry,
            "raffle_collection": user_entry.collection,
            "raffle_description": user_entry.description,
        }
        template = "raffle/prize.html"

        return render(request, template, context)

    if request.method == "POST":
        form_data = {
            "collection": request.POST["collection"],
            "description": request.POST["description"],
            "user_profile": user_profile,
            "won": True,
        }
        entry_form = UserEntryForm(form_data)
        if entry_form.is_valid():
            entry_form = entry_form.save()
            messages.success(request, "Successfully entered raffle!")
            return redirect("home")
        else:
            entry_form = UserEntryForm()
            messages.error(
                request,
                "Failed to enter raffle \
                Please ensure the form is valid.",
            )
    else:
        entry_form = UserEntryForm()

    template = "raffle/raffle.html"
    context = {"entry_form": entry_form}

    return render(request, template, context)


def raffle_login(request):
    """shows error message and redirects user if they are not logged in"""
    messages.error(
        request, "You need to be signed in to register for the raffle!"
    )
    return redirect("home")
