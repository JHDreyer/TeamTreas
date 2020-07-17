from django.shortcuts import render

# Create your views here.
from explore.models import Business


def index(request):
    # use save to add save a new business
    options = Business.objects.all()
    return render(request, 'index_explore.html', {'options': options})
