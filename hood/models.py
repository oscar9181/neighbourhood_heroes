from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    health_email = models.EmailField(max_length=100,default='')
    health_center=models.CharField(max_length=100,default='')
    health_contact = models.IntegerField(default=0, null=True, blank=True)
    police_email = models.EmailField(max_length=100,default='')
    police_center=models.CharField(max_length=100,default='')
    police_contact = models.IntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.name
    def create_neighborhood(self):
        """
        A method that creates a neighbourhood
        """
        self.save()  
        
    def create_neighborhood(self):
        """
        A method that creates a neighbourhood
        """
        self.save()

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)
    phone_no = models.IntegerField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='neighbour', blank=True)
    post_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user