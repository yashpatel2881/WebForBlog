from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=122)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

