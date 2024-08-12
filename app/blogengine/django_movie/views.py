from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render, redirect

from .forms import ReviewsForm , RatingForm
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
        context['star_form'] = RatingForm()
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

class JsonFilterMoviesView(ListView):
    """Фильтр фильмов в json"""

    def get_queryset(self):
        queryset = Movie.objects.all()  # Начинаем с полного списка фильмов

        # Фильтрация по годам
        years = self.request.GET.getlist("year")
        if years:
            queryset = queryset.filter(year__in=years).distinct().values("title", "tagline", "url", "poster")

        # Фильтрация по жанрам
        genres = self.request.GET.getlist("genre")
        if genres:
            queryset = queryset.filter(genres__name__in=genres).distinct().values("title", "tagline", "url", "poster")

        return queryset


    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)


class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
