from django import forms
from .models import *


class form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(), required=True)
    city = forms.CharField(widget=forms.TextInput(), required=False, max_length=50)
    marks = forms.CharField(widget=forms.NumberInput(), required=True, max_length=50)

    class Meta:
        model = student
        fields = ['name', 'email', 'city', 'marks']
