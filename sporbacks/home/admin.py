from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(sosyal_media)
class club_data(admin.ModelAdmin):
    list_display = ("takim_isim","takim_isim_kisaltma","takim_logo")
admin.site.register(clubs, club_data)
admin.site.register(club_point)