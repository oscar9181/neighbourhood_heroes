from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout


from django.contrib import messages

# Create your views here.

def home (request):
    
    
    return render(request,'neighbour/home.html')

def registerpage(request):
    form=CreateUserForm()
    
    if request.method == 'POST':
         form=CreateUserForm(request.POST)
         if form.is_valid():
             form.save()    
             
             user = form.cleaned_data.get('username')
             messages.success(request,'Account has been created for' + user)    
             return redirect('login')    
                   
                   
    context={'form':form}
    return render(request,'neighbour/register.html',context)


def loginpage (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')
             
        
    return render(request,'neighbour/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
