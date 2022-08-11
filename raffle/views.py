from django.shortcuts import render
from django.contrib import messages
from .forms import UserEntryForm
from profiles.models import UserProfile


# Create your views here.
def raffle_entry(request):
    """Add a raffle entry"""
    if request.method == 'POST':
        form = UserEntryForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user.id)
                UserEntryForm.user_profile = profile
                form.save()
            messages.success(request, 'Successfully entered raffle!')
            return render(request, "home/index.html")
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = UserEntryForm()

    template = "raffle/raffle_entry.html"
    context = {
        "form" : form
    }

    return render(request, template, context)


