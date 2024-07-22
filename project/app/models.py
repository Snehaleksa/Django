from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Student(models.Model):
    Name =models.CharField(max_length=100,null=True,blank=True)
    Age =models.IntegerField(null=True,blank=True)
    Phone =models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.Name
    

class Class(models.Model):
    Name =models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=100,null=True,blank=True)
    Age =models.IntegerField(null=True,blank=True)
    Date=models.CharField(max_length=100,null=True,blank=True)
    District=models.CharField(max_length=100,null=True,blank=True)
    Phone =models.IntegerField(null=True,blank=True)
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password =models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.Name
    
        
class Jangomodels(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField()
    username = models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.name   
    

class CustomUser(AbstractUser):
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    image = models.FileField()
    

    def __str__(self):
        return self.username
