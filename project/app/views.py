from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.http import HttpResponse
from .models import Student
from .models import Class

# Create your views here.
def name(request,a):
    if (a==a[::-1]):
      return HttpResponse("Palindrom")
    else:
       return HttpResponse("Not palindrom")


def index(request,b):
   count=0
   vowels=("aeiou")
   for Char in b:
      if Char in vowels:
         count +=1
   return HttpResponse(count)  

def largest(request,a):
      a=[1,2,12,8,7,9]
      largest_numbers=sorted(a,reverse=True)[:3]
      return HttpResponse( largest_numbers)
      



def registration(request):
   if request.method=='POST':
      name=request.POST['name']
      age=request.POST['age']
      phone=request.POST['phonenumber']
      data = Student.objects.create(Name=name,Age=age,Phone=phone)
      data.save()
      return redirect(show)
   else:
      return render(request,'registration.html')


   


def form1(request):
   if request.method=='POST':
      name=request.POST['name']
      gender=request.POST['gender']
      age=request.POST['age']
      date=request.POST['date of birth']
      district=request.POST['district']
      phonenumber=request.POST['phonenumber']
      username=request.POST['username']
      password=request.POST['password']
      data=Class.objects.create(Name=name,Gender=gender,Age=age,Date=date,District=district,Phone=phonenumber,Username=username,Password=password)
      data.save()
      return redirect(show1)
   else:
      return render(request,'form1.html')
   

def show(request):
      data=Student.objects.all()
      return render(request,'show.html',{'data1':data})


def search(request):
   if request.method=='POST':
      search =request.POST['search']
      data=Student.objects.filter(Name=search)
      return render(request,'show.html',{'data1':data})
   else:
      return redirect(show)
def show1(request): 
      data=Class.objects.all()
      return render(request,'show1.html',{'data2':data})
def search1(request):
   if request.method=='POST':
    search1 =request.POST['search1']
    data=Class.objects.filter(Name=search1)
   
    return render(request,'show1.html',{'data2':data})
   else:
      return redirect(show1)   

def edit(request,id):
    data=Student.objects.get(id=id) 
    if request.method=='POST':
        data.Name=request.POST['name']
        data.Age=request.POST['age']
        data.Phone=request.POST['phonenumber']
        data.save()
        return redirect(show)
    else:
        return render(request,'edit.html',{'data':data})
    
def delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect(show)

def edit1(request,id):
    data=Class.objects.get(id=id)
    if request.method=='POST':
        data.Name=request.POST['name']
        data.Gender=request.POST['gender']
        data.Age=request.POST['age']
        data.Date=request.POST['date of birth']
        data.District=request.POST['district']
        data.Phone=request.POST['phone number']
        data.Username=request.POST['username']
        data.Password=request.POST['password']
        data.save()
        return redirect(show1)
    else:
       return render(request,'edit1.html',{'data':data})

def delete1(request,id):
   data=Class.objects.get(id=id)
   data.delete()
   return redirect(show1)

def register(request):
   if request.method=='POST':
     print("====")
     form =RegisterForm()
     print("1234")
     if form.is_valid():
         print("789")
         first_name =form.cleaned_data['first_name']
         print(first_name)
         last_name =form.cleaned_data['last_name']
         email =form.cleaned_data['email']
         username =form.cleaned_data['username']
         password =form.cleaned_data['password']
         data =User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
         data.save()
         print(data)
         return HttpResponse("Successfully registerd")
     else:
         print("----")
         form =RegisterForm()
         return render(request,'form.html',{'form': form})
     
   else:
      print('++++')
      form =RegisterForm()  
      return render(request,'form.html',{'form': form})
