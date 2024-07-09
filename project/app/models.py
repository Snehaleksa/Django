from django.db import models

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
    Date=models.IntegerField(null=True,blank=True)
    District=models.CharField(max_length=100,null=True,blank=True)
    Phone =models.IntegerField(null=True,blank=True)
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password =models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.Name
    
        
