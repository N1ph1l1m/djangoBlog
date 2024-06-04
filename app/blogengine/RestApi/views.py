from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .serializers import WomenSerializer
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.response import Response

from .models import *

# Create your views here.


def test(request):
    return HttpResponse("Test app")


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



class WomenAPIView(APIView):
    def get(self,request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self,request):
        post_new = Women.objects.create(
            title = request.data['title'],
            content  = request.data['content'],
            cat_id = request.data['cat_id']
        )#добавление записи в бд
        return Response({'post': model_to_dict(post_new)}) #возвращает результат
