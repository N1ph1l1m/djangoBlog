from django.shortcuts import render
from rest_framework import generics,viewsets
from django.http import HttpResponse
from .serializers import WomenSerializer
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework import status

from .models import *


# Create your views here.


def test(request):
    return HttpResponse("Test app")


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenApiList(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenApiUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#          #добавление записи в бд
#         return Response({'post': serializer.data})  #возвращает результат
#     def put(self,request,*args,**kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"Method PUT now allowed"})
#
#         try:
#             instance  = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except Women.DoesNotExist:
#             return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         instance.delete()
#         return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
