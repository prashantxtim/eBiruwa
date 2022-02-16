from django.contrib import admin
from django.urls import path
from donateform import views

urlpatterns = [


    path('dform', views.dform),
    path('index', views.index),




]
