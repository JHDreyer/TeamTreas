from django.shortcuts import render

# Create your views here.

def index(request):
    # use save to add save a new business
    return render(request, 'basic.html')
