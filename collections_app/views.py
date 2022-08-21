"""collections views"""
from django.shortcuts import render
from products.models import Collection

# Create your views here.
def collections(request):
    """a view to display all collections"""

    collections_objects = Collection.objects.all()

    context = {
        "collections": collections_objects,
    }

    return render(request, "collections_app/collections.html", context)
