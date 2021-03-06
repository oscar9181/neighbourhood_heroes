from django.contrib.auth.forms import UserCreationForm
from.models import Business, User,NeighbourHood,Profile
from.models import User,NeighbourHood,Profile, Business
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

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

class BusinessForms(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model =  Business
        fields = ['name','email','business_image','location']
