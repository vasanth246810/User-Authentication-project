from datetime import datetime
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.CharField(max_length=150, unique=True)  # Save username as string
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    created_on= models.DateTimeField(default=datetime.now, blank=True)
    email= models.EmailField(max_length=254, blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.user
        
