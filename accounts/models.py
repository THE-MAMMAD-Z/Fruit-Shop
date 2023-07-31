from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    phone=models.IntegerField(default=0)
    email=models.EmailField(default=None)
    address=models.TextField(default=None)

    # name=models.CharField(max_length=100)
    # family=models.CharField(max_length=100)
    profileimage=models.ImageField(upload_to="fruits/")
    man=1
    woman=2
    status_choices=((man,"man"),(woman,"woman"))
    Gender=models.IntegerField(choices=status_choices)
    
  


