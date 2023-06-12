from django import forms

from .models import TastModel , Profile

class TaskForm(forms.Form):
    
    class Meta:
        model= TastModel
        fields = 'task_text'
        
        
class ProfileForm(forms.Form):
    
    class Meta:
        model = Profile
        fields = "__all__"