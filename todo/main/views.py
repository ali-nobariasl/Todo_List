from django.shortcuts import render

from .models import TastModel


def index(request):
    
    
    tm = TastModel.objects.all()
    context = {'tm':tm}
    return render(request,'main/index.html',context= context)
