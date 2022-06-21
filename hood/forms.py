from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from.models import Business, User,NeighbourHood,Profile
=======
from.models import User,NeighbourHood,Profile, Business
>>>>>>> d48b1df3f89cf43bfe8cd3a131b2ca78528a3c73
from django import forms


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio','email','phone_no']

class NeighbourForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields=['name','location','description','image','health_center','health_contact','health_email','police_center','police_contact','police_email']         

<<<<<<< HEAD
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'
=======

class BusinessForms(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model =  Business
        fields = ['name','email','business_image','location']
>>>>>>> d48b1df3f89cf43bfe8cd3a131b2ca78528a3c73
