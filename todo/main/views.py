from django.shortcuts import render, redirect

from .models import TastModel
from .forms import TaskForm

def index(request):
    
    
    tm = TastModel.objects.all().order_by('modified_at')
    context = {'tm':tm}
    return render(request,'main/index.html',context= context)


def taskDone(request,pk):
    
    item = TastModel.objects.get(pk=pk)
    item.completed = True
    item.save()
    return redirect('index')

def taskUnDone(request,pk):
    item = TastModel.objects.get(pk=pk)
    item.completed = False
    item.save()
    return redirect('index')

def deleteTast(request,pk):
    item = TastModel.objects.get(pk=pk)
    item.delete()
    return redirect('index')

def newTask(request):
    
    if request.method == 'POST':
        task_text = request.POST.get('text')
        if task_text:
            item= TastModel.objects.create(task_text=task_text)
            item.save()
            print('saved')
            
    return redirect('index')


def editTask(request,pk):
    
    item = TastModel.objects.get(pk=pk)
    form = TaskForm()
    context = {'item':item}
    print(item)
    print(pk)
    return render(request,'main/edit.html',context=context)