from django.urls import path
from django.shortcuts import HttpResponse
from .views import home


urlpatterns = [
    path("",home,name="home")
]