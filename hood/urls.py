from django.urls import  URLPattern, path

from hood.views import loginpage
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('login/',views.loginpage,name='login'),    
    path('register/',views.registerpage,name='register'),
    path('logout/',views.logoutUser,name= 'logout'),    
           
]