from django.shortcuts import render
from .models import Product, HomepageMedia


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

    menu_categories = [
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
            "menu_categories": menu_categories,
        }
    )


def pastries(request):

    pastry_products = Product.objects.filter(
        category="pastries",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {"pastry_products": pastry_products},
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
