from django import forms



class RegisterForm(forms.Form):
    first_name =forms.CharField(max_length=30)
    last_name =forms.CharField(max_length=30)
    email =forms.CharField()
    username =forms.CharField(max_length=30)
    password =forms.CharField(widget=forms.PasswordInput)