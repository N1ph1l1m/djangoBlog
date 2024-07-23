from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render
from .models import *
# Create your views here.
def test(request):
    return HttpResponse("Test django_movie")


class MovieView(ListView):

    model = Movie
    queryset = Movie.objects.filter(draft = False)
    template_name = "movies/movie_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


