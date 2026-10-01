from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("cakes/", views.cakes, name="cakes"),
    path("pastries/", views.pastries, name="pastries"),
    path("pancakes/", views.pancakes, name="pancakes"),
    path("namkeen/", views.namkeen, name="namkeen"),
    path("snacks/", views.snacks, name="snacks"),
    path("sandwiches/", views.sandwiches, name="sandwiches"),
    path("cookies/", views.cookies, name="cookies"),
]
