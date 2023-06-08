from django import forms

from .models import TastModel

class TaskForm(forms.Form):
    
    class Meta:
        model= TastModel
        fields = 'task_text'