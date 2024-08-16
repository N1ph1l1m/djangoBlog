import django
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
      path('', views.test, name='test'),
      path('films/', views.MovieView.as_view(),name='main_film'),
      path('search/', views.SearchMovie.as_view(), name='search_movie'),
      path('films/filter/', views.FilterMovieView.as_view(), name='filter'),
      path('add-rating/',views.AddStarRating.as_view(),name='add_rating'),
      path('json-filter/',views.JsonFilterMoviesView.as_view(), name='json_filter'),
      path('<slug:slug>/', views.MovieDetailView.as_view(),name='movie_detail'),
      path('review/<int:pk>/', views.AddReview.as_view(),name='add_review'),
      path('actor/<str:slug>/', views.ActorDetailView.as_view(),name='actor_detail'),

]
