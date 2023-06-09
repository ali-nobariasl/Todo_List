from django.db import models


class TastModel(models.Model):
    
    task_text = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task_text