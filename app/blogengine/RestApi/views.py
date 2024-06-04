from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .serializers import WomenSerializer
from .models import *

# Create your views here.


def test(request):
    return HttpResponse("Test app")


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
