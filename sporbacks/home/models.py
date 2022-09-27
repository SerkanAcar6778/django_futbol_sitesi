from distutils.command.upload import upload
from email.policy import default
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
    takim_logo = models.ImageField(upload_to='takim_resim/', default='takim_resim/mnc.png' ,blank = True,null = True,verbose_name='Takım Resmi Ekle')

class club_point(models.Model):
    takim = models.OneToOneField(clubs, models.CASCADE)
    point = models.BigIntegerField()
    win = models.BigIntegerField()
    loss = models.BigIntegerField()