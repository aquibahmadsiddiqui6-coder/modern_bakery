from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("cakes/", views.cakes, name="cakes"),
    path("pastries/", views.pastries, name="pastries"),
    path("pancakes/", views.pancakes, name="pancakes"),
    path("breads-buns/", views.breads_buns, name="breads_buns"),
    path("namkeen/", views.namkeen, name="namkeen"),
    path("snacks/", views.snacks, name="snacks"),
    path("sandwiches/", views.sandwiches, name="sandwiches"),
    path("burgers/", views.burgers, name="burgers"),
    path("cookies/", views.cookies, name="cookies"),
    path("gifts/", views.gifts, name="gifts"),
    path("tea/", views.tea, name="tea"),
    path("cart/", views.cart, name="cart"),
    path("cart/add/", views.add_to_cart, name="add_to_cart"),
    path("cart/update/", views.update_cart, name="update_cart"),
    path("cart/remove/", views.remove_from_cart, name="remove_from_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order/<str:order_id>/", views.order_success, name="order_success"),
]
