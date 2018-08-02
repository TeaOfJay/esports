from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

#from esports.views import index
from django.views.generic import TemplateView

from .views import list
from .views import index

app_name='dotadb'
urlpatterns = [
    url(r'^$'     , index, name="index"),
    url(r'^list/$', list, name="list")
]