from django.db import models

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=80)
    Date_of_release = models.DateField(auto_now=True)
    Music_Type = (
        ('Classic', 'Classic'),
        ('Pop', 'Pop'),
        ('Western', 'Western'),
        ('Melody', 'Melody'),

    )
    genre = models.CharField(max_length=10,choices=Music_Type)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)

    def __str__(self):
        return  self.album_name


class Musicians(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    song_name= models.CharField(max_length=100)
    Instru_Type = (
        ('Vilon', 'Vilon'),
        ('Piano', 'Piano'),
        ('Drums', 'Drums'),
        ('Flute','Flute'),

    )
    music_type = models.CharField(max_length=10,choices=Instru_Type)

    def __str__(self):
        return  self.song_name
