from django.urls import path
from .views import *


urlpatterns = [
      path('', test, name = 'test'),
      path('api/womenlist/', WomenAPIView.as_view()),
      path('api/womenlist/<int:pk>/', WomenAPIView.as_view()),
      path('api/womenapilist/', WomenAPIView.as_view()),
      path('api/womenapilist/<int:pk>/', WomenAPIView.as_view()),
]
