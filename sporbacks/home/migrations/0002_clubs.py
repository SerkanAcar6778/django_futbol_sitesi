# Generated by Django 3.2.13 on 2022-07-31 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('takim_isim', models.CharField(max_length=200)),
                ('takim_isim_kisaltma', models.CharField(max_length=4)),
                ('takim_logo', models.ImageField(blank=True, default='mnc.png', null=True, upload_to='takim_resim/', verbose_name='Takım Resimi')),
            ],
        ),
    ]