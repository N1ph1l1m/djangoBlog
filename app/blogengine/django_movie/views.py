from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render, redirect

from .forms import ReviewsForm
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

class AddReview(View):

    def post(self,request,pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id = pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())