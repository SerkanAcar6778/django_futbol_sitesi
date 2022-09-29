from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    clup = clubs.objects.all()
    club_point_status = clup_point.objects.all().order_by("-point") # order_by 'sırala' demek, point in önündeki " - " de 'aza doğru' demek
    return render(request,"home_temps/index.html", {"clup": clup, "club_point_status": club_point_status})