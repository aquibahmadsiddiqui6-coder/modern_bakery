from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("cakes/", views.cakes, name="cakes"),
    path("pastries/", views.pastries, name="pastries"),
    path("namkeen/", views.namkeen, name="namkeen"),
]
