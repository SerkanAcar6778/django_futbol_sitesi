from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    clup = clubs.objects.all()
    club_point_status = club_point.objects.all().order_by("-point")
    karsilasma = club_vs.objects.all()
    karsilasma_goster = club_vs.objects.all().order_by("id")
    print(clup)
    tum = []
    zaman = [0]
    for i in range(1, len(clup)):
        zaman.append(i)
    for i in clup:
        tum.append(i)
    if len(karsilasma)<=30:
        for i in clup:
            print(i)
            for m,j in  enumerate(clup):
                print(i,j)
                if club_vs.objects.filter(takim1 = i,takim2 = j,mac_durumu = False) :
                    pass
                else:
                    if i != j :
                        club_vs.objects.create(takim1 = i,takim2 = j,gol1=0,gol2 = 0, mac_durumu = False,tarih = zaman[m])
    karsilasma_goster = club_vs.objects.all().order_by("tarih")
    return render(request,"home_temps/index.html",{"clup":clup,"club_point_status":club_point_status,"karsilasma_goster":karsilasma_goster})

# abcd
#(4-1)! = 6