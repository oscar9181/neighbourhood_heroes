from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender=User)
def create_profile(sender,created,instance, **kwargs):
    if created:
        Profile.objects.create(author=instance)
        
        
@receiver(post_save, sender=User)
def save_person(sender, instance, **kwargs):
    instance.profile.save()