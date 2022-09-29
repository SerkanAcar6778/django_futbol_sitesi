from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def index(request):
    clup = clubs.objects.all()
    club_point_status = clup_point.objects.all().order_by("-point") # order_by 'sırala' demek, point in önündeki " - " de 'aza doğru' demek
    karsilasma = club_vs.objects.all()
    karsilasma_goster = club_vs.objects.all().order_by("id")
    print(clup)
    tum = []
    for i in clup:
        tum.append(i)
    if len(karsilasma) <=5:
        for i in clup:
            print(i)
            for j in clup:
                print(i,j)
                if i != j and i in tum and j in tum:
                    tum.remove(i)
                    tum.remove(j)
                    club_vs.objects.create(takim1=i, takim2=j, gol1=0, gol2=0, mac_durumu=False)
        return redirect("/")
    return render(request,"home_temps/index.html", {"clup": clup, "club_point_status": club_point_status, "karsilasma_goster":karsilasma_goster})
