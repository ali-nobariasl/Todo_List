from django.shortcuts import render



def index(request):
    
    conntaxt = {}
    return render(request,'index.html',contaxt= conntaxt)
