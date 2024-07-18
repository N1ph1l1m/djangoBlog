from django.urls import path
from .views import *

urlpatterns = [
      path('', test, name='test'),
      path('films/', MovieView.as_view(),name="movie_list"),
]