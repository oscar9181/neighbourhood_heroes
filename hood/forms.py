from django.contrib.auth.forms import UserCreationForm
from.models import User,NeighbourHood
from django import forms


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class NeighbourForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields=['name','location','description','image','health_center','health_contact','health_email','police_center','police_contact','police_email']         
 