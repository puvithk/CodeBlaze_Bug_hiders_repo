from django.forms import ModelForm
from django import forms
from .models import Accountdetails

class UploadForm(ModelForm):
    name = forms.TextInput()
    age = forms.NumberInput()
    address = forms.TextInput()
    phone = forms.NumberInput()
    gender =forms.TextInput()
    class Meta:
        model = Accountdetails
        fields = ['name','age','gender','address','phone','acc']