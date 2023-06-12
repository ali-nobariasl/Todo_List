from django.db import models
from django.contrib.auth.models import User

    
class Profile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=10)
    user_picture = models.ImageField(null=True, blank=True, default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

class TastModel(models.Model):
    
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    task_text = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task_text