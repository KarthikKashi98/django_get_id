
from django.contrib import admin
from django.urls import path

from djangoProject6 import settings
from .import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [

   path('', views.taskList, name="task"),
   path('reset', views.reset, name="task1"),
   url(r'^media/(P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
   url('^static/(?P<path>.*)$',{'document_root':settings.STATIC_ROOT}),
]
