from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=True, null=True)
    instagram = models.CharField(max_length=20,blank=True,null=True)
    tiktok = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return str(self.user)