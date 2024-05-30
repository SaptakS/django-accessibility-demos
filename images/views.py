from django.shortcuts import render

from .models import Image


def show_images(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})
