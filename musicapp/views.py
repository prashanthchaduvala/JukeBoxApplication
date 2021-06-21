from django.shortcuts import render

# Third party imports
from rest_framework import generics,mixins

from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny

# local imports
from musicapp.serializers import *
from musicapp.models import *


class CreateAlbumApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'

    'this view is post data for  album and get the records'

    def get_object(self, id):
        try:
            return Album.objects.get(id=id)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, id=None, *args, **kwargs):
        if id:
            calobj = self.get_object(id)
            serializer = AlbumSerializer(calobj)
            return Response(serializer.data)
        else:
            alldata = Album.objects.all()
            serializer = AlbumSerializer(alldata, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            save_data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AlbumDetailApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'

    '''get the single record for Album with and delete particular album ,
     update single update and multiple update for album and choice fileds'''

    def get_object(self, id):
        try:
            return Album.objects.get(id=id)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, id=None, *args, **kwargs):
        if id:
            calobj = self.get_object(id)
            serializer = AlbumSerializer(calobj)
            return Response(serializer.data)
        else:
            alldata = Album.objects.all()
            serializer = AlbumSerializer(alldata, many=True)
            return Response(serializer.data)

    def put(self, request, id=None, *args, **kwargs):
        calobj = self.get_object(id)
        serializer = AlbumSerializer(calobj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            body_data = serializer.data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            Album.objects.filter(id=id).delete()
            message = {"success": "delete success"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class MucicAlbumApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Musicians.objects.all()
    serializer_class = MusicianSerializer
    lookup_field = 'id'

    'this view is post data for  musician and get the records'

    def get_object(self, id):
        try:
            return Musicians.objects.get(id=id)
        except Musicians.DoesNotExist:
            raise Http404

    def get(self, request, id=None, *args, **kwargs):
        if id:
            calobj = self.get_object(id)
            serializer = MusicianSerializer(calobj)
            return Response(serializer.data)
        else:
            alldata = Musicians.objects.all()
            serializer = MusicianSerializer(alldata, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            save_data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MusicDetailApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Musicians.objects.all()
    serializer_class = MusicianSerializer
    lookup_field = 'id'

    '''get the single record for music with fk (album) and delete particular music ,
    update single update and multiple update for song and choice fileds'''

    def get_object(self, id):
        try:
            return Musicians.objects.get(id=id)
        except Musicians.DoesNotExist:
            raise Http404

    def get(self, request, id=None, *args, **kwargs):
        if id:
            calobj = self.get_object(id)
            serializer = MusicianSerializer(calobj)
            return Response(serializer.data)
        else:
            alldata = Musicians.objects.all()
            serializer = MusicianSerializer(alldata, many=True)
            return Response(serializer.data)

    def put(self, request, id=None, *args, **kwargs):
        calobj = self.get_object(id)
        serializer = MusicianSerializer(calobj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            body_data = serializer.data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            Musicians.objects.filter(id=id).delete()
            message = {"success": "delete success"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)