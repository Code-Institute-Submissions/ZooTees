from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """a view to view the bag contetnts page"""

    return render(request, "bag/bag.html")