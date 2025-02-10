from django.shortcuts import render 
from .forms import  LoginForm,CreateUserForm

# Create your views here.


def home(request):  #Home Page
    return render(request,'website/index.html')   

def register(request): 
    form = CreateUserForm()

    if request.method == "POST": 
        form = CreateUserForm(request.POST) 
        if form. is_valid(): 
            form.save() 
            # return redirect('') 

    context = {'form': form}
               
    return render(request, 'website/register.html', context=context) 
 



