from django import forms
from .models import Jangomodels



class RegisterForm(forms.Form):
    first_name =forms.CharField(max_length=30)
    last_name =forms.CharField(max_length=30)
    email =forms.CharField()
    username =forms.CharField(max_length=30)
    password =forms.CharField(widget=forms.PasswordInput)


class JangomodelForm(forms.ModelForm):
    class Meta:
        model =Jangomodels
        fields ='__all__'    