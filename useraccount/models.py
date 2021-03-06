from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return str(self.user)
        
@receiver(post_save,sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)