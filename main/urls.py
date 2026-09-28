from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cakes/", views.cakes, name="cakes"),
    path("pastries/", views.pastries, name="pastries"),
]
