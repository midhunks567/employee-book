from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .form import Empforms

from .models import Emp


# Create your views here.
from django.views.generic import ListView, DetailView, UpdateView, DeleteView



def register(request):
    if request.method=='POST':
        username=request.POST['usrnm']
        email = request.POST['email']
        password1 = request.POST['psw1']
        password2 = request.POST['psw2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save();
                print("user created")
            return redirect('/')
        else:
            # print("password not matched")
            messages.info(request,"password not matched")
            return redirect('register')
    else:
        return render(request,'registration.html')


def login(request):
    if request.method=="POST":
        username=request.POST['usrnm']
        password = request.POST['psw1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('add')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')




def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        emp_id=request.POST.get('emp_id')
        occup=request.POST.get('occup')
        obj=Emp(name=name,emp_id=emp_id,occup=occup)
        obj.save()
    return render(request,'add.html')
def emp_view(request):
    obj1 = Emp.objects.all()
    return render(request,'detail.html',{'obj1':obj1})

def delete(request,empid):
    emp=Emp.objects.get(id=empid)
    if request.method=='POST':
        emp.delete()
        return redirect('detail')
    return render(request,'delete.html',{'task':emp})

def update(request,id):
    emp=Emp.objects.get(id=id)
    form=Empforms(request.POST or None,instance=emp)
    if form.is_valid():
        form.save()
        return redirect('detail')
    return render(request,'edit.html',{'task':emp,'form':form})