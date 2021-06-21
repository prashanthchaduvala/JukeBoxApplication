from rest_framework import serializers
from musicapp.models import *

# Album
class AlbumSerializer(serializers.ModelSerializer):
    album_name = serializers.CharField(min_length=5,max_length=80)
    class Meta:
        model = Album
        fields = '__all__'
        # fields = ['album_name','Date_of_release','Music_Type','genre','price','description']


# Musician
class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicians
        fields = '__all__'