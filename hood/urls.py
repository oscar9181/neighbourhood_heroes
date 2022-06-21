from django.urls import  URLPattern, path

from hood.views import loginpage
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('login/',views.loginpage,name='login'),    
    path('register/',views.registerpage,name='register'),
    path('logout/',views.logoutUser,name= 'logout'),
    path('profile/',views.userprofile,name='profile'),
    path('community/',views.community,name='community'),
    path('hood/<str:pk>/',views.view,name='hood'),       
    path('update/',views.update,name='update'),
    path('search/',views.search,name='search'),
    path('business/',views.bizz,name='business'),
]