from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm


def test(request):
    return HttpResponse("Test django_movie")



class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_ur = '/'
