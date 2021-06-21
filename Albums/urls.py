"""Albums URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from musicapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # album url
    path('add/album/', views.CreateAlbumApiView.as_view(), name='list_create'),
    path('album/detail/<int:id>/', views.AlbumDetailApiView.as_view(),name='delete_retrive' ),

    # musician url
    path('add/musician/', views.MucicAlbumApiView.as_view(), name='music_list_create'),
    path('music/detail/<int:id>/', views.MusicDetailApiView.as_view(),name='music_delete_retrive' ),

]
