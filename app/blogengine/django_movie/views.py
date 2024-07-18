from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from .models import *
# Create your views here.
def test(request):
    return HttpResponse("Test django_movie")


class MovieView(View):
    def get(self,request):
        movies = Movie.objects.all()
        return render(request,"movies/movie_list.html",{"movie_list":movies})

