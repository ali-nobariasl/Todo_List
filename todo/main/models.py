from django.db import models


class TastModel(models.Model):
    
    task_text = models.TextField()