from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):
    date= datetime.datetime.now()
    print("test function is called from view ")
    return render(request, "home.html",{})

def about(request):
     return render(request, "about.html",{})

def services(request):
     return render(request, "services.html",{})