from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Picture

# Create your views here.


def pictures(request):

    pictures = Picture.objects.all()

    return render(request, 'pictures.html', {"pictures": pictures})


def search_results(request):
    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Picture.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
