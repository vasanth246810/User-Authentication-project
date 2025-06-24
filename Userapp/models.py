from datetime import datetime
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.CharField(max_length=150, unique=True)  
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    created_on= models.DateTimeField(default=datetime.now, blank=True)
    email= models.EmailField(max_length=254, blank=True)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.user
        
