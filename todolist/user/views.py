from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .forms import AddreminderForm,SignUpForm,LoginForm
from django.contrib import messages
from .models import AddReminder
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
# Create your views here.


def signin_required(fun):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            messages.error(request,"Login Required Firthis Action")
            return redirect('signin')
    return inner
 

@method_decorator(signin_required,name='dispatch')
class Addreminder(View):
    def get(self,request):
        form=AddreminderForm()
        return render (request,'addreminder.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form_data=AddreminderForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Reminder added successfully !!!")
            return redirect("viewreminder")
        else:
            return render(request,"addreminder.html",{"form":form_data})

@method_decorator(signin_required,name='dispatch')       
class viewreminder(View):
    def get(self,request,*args,**kwargs):
         rmdr=AddReminder.objects.all()
         return render(request,'viewreminder.html',{'data':rmdr})

@method_decorator(signin_required,name='dispatch')   
class DeleteReminder(View):
    def get(self,request,*args,**kwargs):
        rid=kwargs.get('rid')
        rmdr=AddReminder.objects.get(id=rid)
        rmdr.delete()
        messages.success(request,'Reminder Deleted')
        return redirect('viewreminder')

@method_decorator(signin_required,name='dispatch')    
class updateRem(View):
    def get(self,request,*args,**kwargs):
        rid=kwargs.get("rid")
        rmdr=AddReminder.objects.get(id=rid)
        form=AddreminderForm(instance=rmdr)
        return render(request,'updatereminder.html',{'form':form})
    def post(self, request,*args,**kwargs):
        rid=kwargs.get("rid")
        rmdr=AddReminder.objects.get(id=rid)
        form_data=AddreminderForm(data=request.POST,instance=rmdr)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Reminder updated successfully")
            return redirect('viewreminder')
        else:
            return render(request,'updatereminder.html',{'form':form_data})
        
class SignUp(View):
    def get(self,request):
        form=SignUpForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request):
        form_data=SignUpForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Registration is Successfull ")
            return redirect('signin')
        else:
            return render(request,"signup.html",{'form':form_data})
        

class Signin(View):
    def get(self,request,*args,**kwrags):
        form=LoginForm()
        # us=request.user
        return render(request,'signin.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Sign in completed ")
                return redirect('viewreminder')
            else:
                messages.error(request,"Invalid Username or Password")
                return render(request,'signin.html',{'form':form_data})
            
        else:
            
            return render(request,'signin.html',{'form':form_data})

@method_decorator(signin_required,name='dispatch')        
class lgout(View):
     def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')
        