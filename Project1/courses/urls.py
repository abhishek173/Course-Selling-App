from django.urls import path
from django.shortcuts import HttpResponse
from courses.views.homepage import home


urlpatterns = [
    path("",home,name="home")
]