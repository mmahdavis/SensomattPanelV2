"""sensomatt URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'panel'
urlpatterns = [
    re_path(r'notification/(?P<token>\d+)', views.notification),
    re_path(r'numberofbed/(?P<token>\d+)', views.numberofbed),
    re_path(r'patientinfo/(?P<token>\d+)/(?P<patientId>\d+)', views.patientinfo),
    re_path(r'patientstatus/(?P<token>\d+)/(?P<bedId>\d+)', views.patientstatus),
    re_path(r'bedanalyses/(?P<token>\d+)/(?P<bedId>\d+)', views.bedanalyses),
    re_path(r'suggestions/(?P<token>\d+)/(?P<bedId>\d+)', views.suggestions),
    re_path(r'bedhistory/(?P<token>\d+)', views.bedhistory),
    re_path(r'dashboard/(?P<token>\d+)', views.dashboard),
]
