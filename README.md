# JukeBoxApplication
creating music album

intsall requirements 
1) python 3.9
2) django 3.2
3) djangorestframework 3.12
4) default django db(sqlite 3)


create django project use commands
  django-admin startproject projectname
  django-admin startproject appname
  
  if change database add new db in settings 
     eg :
     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

change this db

add any third party installs eg ;rest_framework ,app names
add in installed apps 
