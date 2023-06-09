from django.urls import path 

from .views import index , taskDone ,newTask ,deleteTast ,taskUnDone



urlpatterns = [
    
    path('',index, name='index'), 
    
    path('taskeDone/<int:pk>/', taskDone, name='taskeDone' ),
    path('taskUnDone/<int:pk>', taskUnDone, name='taskUnDone' ),
    
    path('newTask/', newTask, name='newTask' ),
    path('deleteTast/<int:pk>', deleteTast, name='deleteTast' ),
      
]
