from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def name(request,a):
    if (a==a[::-1]):
      return HttpResponse("Palindrom")
    else:
       return HttpResponse("Not palindrom")