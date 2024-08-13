from django.contrib import admin
from .models import Contact
from django import forms


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email","data")