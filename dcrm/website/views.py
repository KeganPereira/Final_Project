from django.shortcuts import render,redirect
from .forms import  LoginForm,CreateUserForm 
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate

# Create your views here.


def home(request):  #Home Page
    return render(request,'website/index.html')   

def register(request): 
    form = CreateUserForm()

    if request.method == "POST": 
        form = CreateUserForm(request.POST) 
        if form. is_valid(): 
            form.save() 
            return redirect('my-login') 

    context = {'form': form}
               
    return render(request, 'website/register.html', context=context)  

def my_login(request): 
    form= LoginForm() 

    if request.method == "POST":
       form= LoginForm(request, data=request.POST) 

       if form.is_valid(): 
           username =  request.POST.get('username') 
           password = request.POST.get('password') 

           user = authenticate(request, username=username, password=password) 

           if user is not None: 
               auth.login(request,user) 
               return redirect('')  
    context ={'login_form':form} 
    return render(request, 'website/login.html', context=context)  

def logout(request): 
    auth.logout(request) 
    return redirect("")

        
       



