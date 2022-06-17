from django.shortcuts import render

# Create your views here.

def home (request):
    
    
    return render(request,'neighbour/home.html')

def registerpage (request):
    
    return render(request,'neighbour/register.html')


def loginpage (request):
    
    return render(request,'neighbour/login.html')