from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    clup = clubs.objects.all()
    club_point_status = club_point.objects.all().order_by("-point") # order_by 'sırala' demek, point in önündeki " - " de 'aza doğru' demek
    karsilasma = club_vs.objects.all()
    if len (karsilasma)==15:
        pass
    else:
        for i in clup:
            for j in clup:
                if i.id == j.id:
                    pass
                else:
                    club_vs.objects.create(i)
        return redirect("/")
    return render(request,"home_temps/index.html", {"clup": clup, "club_point_status": club_point_status})