from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
   return render(request, "myapp/index.html",{})


def userreg(request):
    return render(request, "myapp/userreg.html", {})
 
def insertuser(request):
     vuid = request.POST['tuid'];
     vuname= request.POST['tuname'];
     vuemail= request.POST['tuemail'];
     vucontact= request.POST['tucontact']; 
     us=User(uid=vuid, uname=vuname, uemail=vuemail, ucontact=vucontact);
     us.save();
     return render(request, 'myapp/index.html', {})

 
 


