from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    clup = clubs.objects.all()
    return render(request,"home_temps/index.html", {"clup": clup})