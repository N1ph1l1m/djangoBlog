from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("email",)
        widget = {
            "email": forms.TextInput(attrs={"class":"editContent", "placeholder":"Your email...... "})
        }
        labels = {
            "email":''
        }