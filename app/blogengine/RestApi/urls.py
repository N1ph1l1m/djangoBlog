from django.urls import path
from .views import *


urlpatterns = [
      path('', test, name='test'),
      # path('api/womenlist/', WomenAPIView.as_view()),
      # path('api/womenlist/<int:pk>/', WomenAPIView.as_view()),
      path('api/womenlist/', WomenApiList.as_view()),
      path('api/womenlist/<int:pk>/', WomenApiUpdate.as_view()),
      path('api/womendetail/<int:pk>/', WomenApiDetailView.as_view()),
]
