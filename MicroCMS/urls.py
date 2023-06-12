from django.contrib import admin
from django.urls import path,include
from . views import showAllDevices,GenerateToken
urlpatterns = [
    path("alldevices/",showAllDevices), # To get all the available_devices for the current site url
    path("createtoken/",GenerateToken) # to generate walk-in token number
    ]