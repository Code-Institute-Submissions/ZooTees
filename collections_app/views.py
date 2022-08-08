from django.shortcuts import render, get_object_or_404
from products.models import Collection

# Create your views here.
def collections(request):
    """a view to display all collections"""

    collections = Collection.objects.all()

    context = {
        "collections": collections,
    }

    return render(request, "collections_app/collections.html", context)
