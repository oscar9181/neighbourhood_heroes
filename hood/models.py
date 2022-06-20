from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

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
    profile_picture = CloudinaryField('image',default='default.jpg')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)
    phone_no = models.IntegerField(blank=True,null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='neighbour', blank=True)
    post_date = models.DateTimeField(auto_now=True)
    
    
    
def __str__(self):
        return f'{self.user.username} Profile'
    
# class Business(models.Model):
#     name = models.CharField(max_length=200)
#     image = CloudinaryField('image')
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     email =  models.CharField(max_length=60)
#     phone_no = models.IntegerField(blank=True)
#     neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE, related_name='business',null=True)
#     post_date = models.DateTimeField(auto_now=True)


class Business(models.Model):
    name =  models.CharField(max_length=100)
    business_owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    business_image = CloudinaryField(null=True)
    business_location = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=100,null=True,blank=True)

    def save_business(self):
        self.save()

    @classmethod
    def delete_business(cls, id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_business(cls, id, new_name):
        cls.objects.filter(id=id).update(name=new_name)

    @classmethod
    def search_by_title(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('business-detail',kwargs={'pk':self.pk})
