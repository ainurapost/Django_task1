from django.shortcuts import render
from .models import Photos


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    with open('pages/templates/pages/about.txt') as f:
        data = f.read()
    file_data = data
    return render(request, 'pages/about.html', {'file_data': file_data})


def contact(request):
    with open('pages/templates/pages/contact.txt') as f:
        data = f.read()
    file_data = data
    return render(request, 'pages/contact.html', {'file_data': file_data})


def gallery(request):
    photos = Photos.objects.all()
    print(photos)
    return render(request, 'pages/gallery.html', {'photos': photos,})

