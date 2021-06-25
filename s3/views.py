from django.shortcuts import render , HttpResponse , redirect
from app.models import *

def index(request):
    data = Super_AdminAccount.objects.get(Fname = "safdar")
    return render(request,'index.html',{'name':data})



    

