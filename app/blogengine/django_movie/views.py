from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render, redirect

from .forms import ReviewsForm
from .models import *


# Create your views here.
def test(request):
    return HttpResponse("Test django_movie")


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MovieView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


class ActorDetailView(GenreYear, DetailView):
    model = Actor
    slug_field = "name"
    template_name = "movies/actor.html"


class AddReview(View):

    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class FilterMovieView(GenreYear, ListView):
    template_name = "movies/movie_list.html"

    def get_queryset(self):
        queryset = Movie.objects.all()  # Начинаем с полного списка фильмов

        # Фильтрация по годам
        years = self.request.GET.getlist("year")
        if years:
            queryset = queryset.filter(year__in=years)

        # Фильтрация по жанрам
        genres = self.request.GET.getlist("genre")
        if genres:
            queryset = queryset.filter(genres__name__in=genres)

        return queryset