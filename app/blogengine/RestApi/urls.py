from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)


urlpatterns = [
      path('', test, name='test'),
      # path('api/womenlist/', WomenAPIView.as_view()),
      # path('api/womenlist/<int:pk>/', WomenAPIView.as_view()),
     # path('api/womenlist/', WomenViewSet.as_view({'get': 'list'})),
      #path('api/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
      #path('api/womendetail/<int:pk>/', WomenApiDetailView.as_view()),
      path('api/v1/',include(router.urls))
]
