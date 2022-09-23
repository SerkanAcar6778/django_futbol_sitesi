from django.db import models

# Create your models here.

class sosyal_media(models.Model):
    isim = models.CharField(max_length=100)
    links = models.CharField(max_length=300)
    def __str__(self) :
        return self.isim