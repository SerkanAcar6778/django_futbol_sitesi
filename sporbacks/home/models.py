from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class sosyal_media(models.Model):
    isim = models.CharField(max_length=100)
    links = models.CharField(max_length=300)
    def __str__(self) :
        return self.isim

class clubs(models.Model):
    takim_isim = models.CharField(max_length=200)
    takim_isim_kisaltma = models.CharField(max_length=4)
    takim_logo = models.ImageField(upload_to='takim_resim/', default="takim_resim/mnc.png" ,blank = True,null = True,verbose_name="Takım Resimi")
    def __str__(self) :
        return self.takim_isim
class club_point(models.Model):
    takim = models.OneToOneField(clubs,models.CASCADE)
    point = models.BigIntegerField()
    win = models.BigIntegerField()
    loss = models.BigIntegerField()

class club_vs(models.Model):
    takim1 = models.ForeignKey(clubs,related_name="takim1" ,blank=True,on_delete=models.CASCADE)
    gol1 = models.BigIntegerField()
    takim2 = models.ForeignKey(clubs,related_name="takim2", blank=True,on_delete=models.CASCADE,null=True)
    gol2 = models.BigIntegerField()
    mac_durumu = models.BooleanField()
    tarih = models.BigIntegerField(null = True)