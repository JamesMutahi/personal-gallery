from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location


# Create your views here.
def index(request):
    return render(request, 'index.html')


def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()
    return render(request, 'gallery.html', locals())


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'results.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'results.html', {"message": message})


def getcat(request, catid):
    category = get_object_or_404(Category, pk=catid)
    title = category.Name
    name = category.Name
    images = category.images.all()
    return render(request, 'results.html', locals())


def get_image_by_location(request, location_name):
    location = Location.objects.all()
    location_name = location_name
    location_images = Image.filter_by_location(location_name)
    return render(request, 'location.html', {"location_images": location_images, "location": location, "location_name" : location_name })
