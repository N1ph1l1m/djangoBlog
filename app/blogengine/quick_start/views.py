from django.http import HttpResponse
from .models import *
from django.shortcuts import render

# Create your views here.



def test(request):
    return HttpResponse("Test quick start")
