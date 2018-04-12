from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

#from esports.views import index
from django.views.generic import TemplateView

app_name='dotadb'
urlpatterns = [
    url(r'^$'     , TemplateView.as_view(template_name='dotadb/index.html'), name="index"),
]