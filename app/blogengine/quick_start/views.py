from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import  User, Group
from .models import Snippet
from   .serializers import  SnippetSerializer
from rest_framework import viewsets
from rest_framework  import permissions
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import  APIView
from rest_framework import mixins
from rest_framework import generics
from .serializers import UserSerializer,GroupSerializer


def test(request):
    return HttpResponse("Test quick start")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

## простой вариант запросов, который привязан к JSON
# @csrf_exempt
# def snippet_list(request):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(request.error, status=400)
#
# @csrf_exempt
# def snippet_detail(request,pk):
#     try:
#         snippet = Snippet.objects.get(pk = pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=400)
#
#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser.parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         snippet.delete()
#         return HttpResponse(status=204)
#






## усовершенственная версия,  запросы не привязанны к определенному типу содержимого
# @api_view(['GET', 'POST'])
# def snippet_list(reqiest, format = None):
#     if reqiest.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#     elif reqiest.method == 'POST':
#         serializer = SnippetSerializer(data=reqiest.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'POST'])
# def snippet_detail(request,pk,format=None):
#     try:
#         snippet = Snippet.object.get(pk = pk)
#     except Snippet.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

# классовое представление
# class SnippetsList(APIView):
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self,request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class SnippetsDetail(APIView):
#
#     def get_objects(self,pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self,requiest, pk, format=None):
#         snippet = self.get_objects(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         snippet = self.get(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         snippet = self.get_objects(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# представление класснов через миксины
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#

#смешанные общие представления
class SnippetsList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer