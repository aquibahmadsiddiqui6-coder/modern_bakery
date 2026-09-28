from django.shortcuts import render
from .models import Product, HomepageMedia


def get_menu_categories():
    return [
        {"slug": "all", "name": "All items", "icon": "✦", "hint": "The full counter"},
        {"slug": "cakes", "name": "Cakes", "icon": "🎂", "hint": "Celebration & cream cakes"},
        {"slug": "pastries", "name": "Pastries", "icon": "🥐", "hint": "Fresh individual treats"},
        {"slug": "biscuits", "name": "Cookies", "icon": "🍪", "hint": "Biscuits & tea-time bites"},
        {"slug": "pizza", "name": "Pizza", "icon": "🍕", "hint": "Hot, cheesy favourites"},
        {"slug": "burgers", "name": "Burgers", "icon": "🍔", "hint": "Loaded savoury bites"},
        {"slug": "sandwiches", "name": "Sandwiches", "icon": "🥪", "hint": "Quick café classics"},
        {"slug": "snacks", "name": "Snacks", "icon": "🍟", "hint": "Savoury bakery snacks"},
        {"slug": "namkeen", "name": "Namkeen", "icon": "🥨", "hint": "Crispy savoury favourites"},
        {"slug": "beverages", "name": "Tea & drinks", "icon": "☕", "hint": "Warm cups & cool sips"},
    ]


def home(request):

    products = Product.objects.filter(
        is_available=True
    )

    featured_videos = HomepageMedia.objects.filter(
        section="shop",
        media_type="video",
        is_active=True
    ).order_by("display_order")[:2]

    shop_media = HomepageMedia.objects.filter(
        section="shop",
        media_type="photo",
        is_active=True
    ).order_by("display_order")

    product_media = HomepageMedia.objects.filter(
        section="products",
        is_active=True
    ).order_by("display_order")

    behind_media = HomepageMedia.objects.filter(
        section="behind",
        is_active=True
    ).order_by("display_order")

    cake_media = HomepageMedia.objects.filter(
        section="cakes",
        media_type="photo",
        is_active=True
    ).order_by("display_order")

    return render(
        request,
        "main/home.html",
        {
            "products": products,
            "featured_videos": featured_videos,
            "shop_media": shop_media,
            "product_media": product_media,
            "behind_media": behind_media,
            "cake_media": cake_media,
            "menu_categories": get_menu_categories(),
            "show_menu_items": False,
        }
    )


def menu(request):
    return render(
        request,
        "main/menu.html",
        {
            "products": Product.objects.filter(is_available=True),
            "menu_categories": get_menu_categories(),
        },
    )


def pastries(request):

    pastry_products = Product.objects.filter(
        category="pastries",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": pastry_products,
            "category_label": "PASTRIES",
            "hero_label": "FRESH FROM THE COUNTER",
            "hero_title": "Pastries made for the moment.",
            "hero_description": "Choose a favourite, then open its gallery to see every available finish and variation.",
            "section_title": "Pick your sweet favourite.",
            "empty_message": "Our pastry counter is being prepared. Please check back soon.",
            "placeholder_icon": "🥐",
        },
    )


def namkeen(request):

    namkeen_products = Product.objects.filter(
        category="namkeen",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": namkeen_products,
            "category_label": "NAMKEEN",
            "hero_label": "FRESH FROM THE COUNTER",
            "hero_title": "Crispy favourites for every craving.",
            "hero_description": "Explore savoury namkeen favourites, then open a product photo to see it up close.",
            "section_title": "Pick your savoury favourite.",
            "empty_message": "Our namkeen counter is being prepared. Please check back soon.",
            "placeholder_icon": "🥨",
        },
    )


def cakes(request):

    cake_media = HomepageMedia.objects.filter(
        section="cakes",
        media_type="photo",
        is_active=True,
    ).order_by("display_order")

    return render(
        request,
        "main/cakes.html",
        {"cake_media": cake_media},
    )
