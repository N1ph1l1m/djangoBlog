import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Women




# ## класс словарь с данными
# class WomenModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content


# ## класс сериализатор для данных.Заголовки должны совподать
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()


# # преобразование данных в JSON формат
# def encode():
#     model = WomenModel('Angelina Lolie', 'Content: Angelina Jolie  - is actor')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data,type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# # class WomenAPIView(APIView):
# #     def get(self,request):
# #         return Response({'title':'Angelina Jolie'})

# ## декодирование полученных данных
# def decode():
#     stream = io.BytesIO(b'{"title":"Mark Spector", "content":"Content : Is kindom moon"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data = data)
#     serializer.is_valid()
#     print(serializer.validated_data)


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only = True)
    time_update = serializers.DateTimeField(read_only = True)
    is_published = serializers.BooleanField(default = True)
    cat_id = serializers.IntegerField()
