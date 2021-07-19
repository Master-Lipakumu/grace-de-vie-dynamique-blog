from django.db import models
from django.contrib.auth.models import User
from blog.models import Pub

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(upload_to ="profile_pics", default="default.jpg")
    pubs = models.ManyToManyField(Pub)