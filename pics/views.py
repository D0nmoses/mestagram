from django.shortcuts import render
from .models import Image

# Create your views here.

def index(request):
    images = Image.all_images()

    return render(request, 'all-pics/index.html',{"images":images})