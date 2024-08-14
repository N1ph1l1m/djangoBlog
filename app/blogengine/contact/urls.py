from django.urls import path,include
from .views import ContactView , test


urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
    path("test/", test, name="test"),

]