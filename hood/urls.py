from django.urls import  URLPattern, path

from hood.views import loginpage, BusinessCreateView, BusinessDeleteView, BusinessDetailView, BusinessListView, BusinessUpdateView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('login/',views.loginpage,name='login'),    
    path('register/',views.registerpage,name='register'),
    path('logout/',views.logoutUser,name= 'logout'),
    path('profile/',views.userprofile,name='profile'),
    path('community/',views.community,name='community'),       
    path('update/',views.update,name='update'),
    path('search/',views.search,name='search'),
    path('',BusinessListView.as_view(),name='home'),
    path('business/<int:pk>/',BusinessDetailView.as_view(), name='business-detail'),
    path('business/new/', BusinessCreateView.as_view(), name='business-create'),
    path('business/<int:pk>/update/',BusinessUpdateView.as_view(), name='business-update'),
    path('business/<int:pk>/delete/',BusinessDeleteView.as_view(),name='business-delete'), 

]