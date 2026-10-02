from django.shortcuts import render
from .models import Product, HomepageMedia


def get_menu_categories():
    return [
        {"slug": "all", "name": "All items", "icon": "✦", "hint": "The full counter"},
        {"slug": "cakes", "name": "Cakes", "icon": "🎂", "hint": "Celebration & cream cakes"},
        {"slug": "pastries", "name": "Pastries", "icon": "🥐", "hint": "Fresh individual treats"},
        {"slug": "pancakes", "name": "Pancakes", "icon": "🥞", "hint": "Fluffy sweet favourites"},
        {"slug": "breads_buns", "name": "Breads & Buns", "icon": "🍞", "hint": "Fresh breads & bakery buns"},
        {"slug": "biscuits", "name": "Cookies", "icon": "🍪", "hint": "Biscuits & tea-time bites"},
        {"slug": "pizza", "name": "Pizza", "icon": "🍕", "hint": "Hot, cheesy favourites"},
        {"slug": "burgers", "name": "Burgers", "icon": "🍔", "hint": "Loaded savoury bites"},
        {"slug": "sandwiches", "name": "Sandwiches", "icon": "🥪", "hint": "Quick café classics"},
        {"slug": "snacks", "name": "Snacks & Patties", "icon": "🍟", "hint": "Savoury bakery snacks & patties"},
        {"slug": "namkeen", "name": "Namkeen", "icon": "🥨", "hint": "Crispy savoury favourites"},
        {"slug": "beverages", "name": "Tea & drinks", "icon": "☕", "hint": "Warm cups & cool sips"},
        {"slug": "gifts", "name": "Gifts & Hampers", "icon": "🎁", "hint": "Thoughtful bakery gifting"},
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
            "hero_image": "/media/hero/pastries-devils-food-cake.jpg",
            "section_title": "Pick your sweet favourite.",
            "empty_message": "Our pastry counter is being prepared. Please check back soon.",
            "placeholder_icon": "🥐",
        },
    )


def pancakes(request):

    pancake_products = Product.objects.filter(
        category="pancakes",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": pancake_products,
            "category_label": "PANCAKES",
            "hero_label": "FRESH FROM THE COUNTER",
            "hero_title": "Fluffy favourites, made to order.",
            "hero_description": "Explore our pancake selection, then open a product photo to see it up close.",
            "hero_image": "/media/hero/pancakes-dessert.jpg",
            "section_title": "Pick your pancake favourite.",
            "empty_message": "Our pancake counter is being prepared. Please check back soon.",
            "placeholder_icon": "🥞",
        },
    )


def breads_buns(request):

    bread_products = Product.objects.filter(
        category="breads_buns",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": bread_products,
            "category_label": "BREADS & BUNS",
            "hero_label": "FRESH FROM THE COUNTER",
            "hero_title": "Fresh breads, soft buns.",
            "hero_description": "Explore our everyday breads and bakery buns, freshly prepared for every meal and tea break.",
            "section_title": "Pick your bakery favourite.",
            "empty_message": "Our bread counter is being prepared. Please check back soon.",
            "placeholder_icon": "🍞",
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
            "hero_image": "/media/hero/namkeen-hero.jpg",
            "section_title": "Pick your savoury favourite.",
            "empty_message": "Our namkeen counter is being prepared. Please check back soon.",
            "placeholder_icon": "🥨",
        },
    )


def snacks(request):

    snack_products = Product.objects.filter(
        category="snacks",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": snack_products,
            "category_label": "SNACKS",
            "hero_label": "FRESH FROM THE COUNTER",
            "hero_title": "Savoury favourites for every craving.",
            "hero_description": "Explore freshly made bakery snacks, then open a product photo to see it up close.",
            "hero_image": "/media/hero/snacks-hero.jpg",
            "section_title": "Pick your savoury favourite.",
            "empty_message": "Our snack counter is being prepared. Please check back soon.",
            "placeholder_icon": "🍟",
        },
    )


def sandwiches(request):

    sandwich_products = Product.objects.filter(
        category="sandwiches",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": sandwich_products,
            "category_label": "SANDWICHES",
            "hero_label": "FRESH FROM THE COUNTER",
            "hero_title": "Fresh sandwiches, made for the moment.",
            "hero_description": "Explore our sandwich selection, then open a product photo to see it up close.",
            "hero_image": "/media/hero/sandwiches-hero.jpg",
            "section_title": "Pick your sandwich favourite.",
            "empty_message": "Our sandwich counter is being prepared. Please check back soon.",
            "placeholder_icon": "🥪",
        },
    )


def burgers(request):

    burger_products = Product.objects.filter(
        category="burgers",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": burger_products,
            "category_label": "BURGERS",
            "hero_label": "FRESH FROM THE COUNTER",
            "hero_title": "Fresh burgers, made to order.",
            "hero_description": "Explore our burger selection, then open a product photo to see every delicious detail.",
            "hero_image": "/media/hero/burgers-hero.jpg",
            "section_title": "Pick your burger favourite.",
            "empty_message": "Our burger counter is being prepared. Please check back soon.",
            "placeholder_icon": "🍔",
        },
    )


def cookies(request):

    cookie_products = Product.objects.filter(
        category="biscuits",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": cookie_products,
            "category_label": "COOKIES",
            "hero_label": "FRESH FROM THE COUNTER",
            "hero_title": "Crisp favourites for every tea break.",
            "hero_description": "Explore buttery cookies and biscuits, then open a product photo to see it up close.",
            "hero_image": "/media/hero/cookies-chocolate-oat-cookies.jpg",
            "section_title": "Pick your tea-time favourite.",
            "empty_message": "Our cookie counter is being prepared. Please check back soon.",
            "placeholder_icon": "🍪",
        },
    )


def gifts(request):

    gift_products = Product.objects.filter(
        category="gifts",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": gift_products,
            "category_label": "GIFTS & HAMPERS",
            "hero_label": "MADE TO GIVE",
            "hero_title": "Beautiful bakery gifts for every occasion.",
            "hero_description": "Explore our gifting collection, thoughtfully prepared for sharing, celebrating, and saying thank you.",
            "hero_image": "/media/hero/gifts-hero.jpg",
            "section_title": "Choose a thoughtful gift.",
            "empty_message": "Our gifting collection is being prepared. Please check back soon.",
            "placeholder_icon": "🎁",
        },
    )


def tea(request):

    tea_products = Product.objects.filter(
        category="beverages",
        is_available=True,
    ).prefetch_related("images")

    return render(
        request,
        "main/pastries.html",
        {
            "category_products": tea_products,
            "category_label": "TEA & DRINKS",
            "hero_label": "FROM THE TEA COUNTER",
            "hero_title": "Warm blends for every pause.",
            "hero_description": "Explore our tea and beverage selection, prepared to bring a little warmth to every break.",
            "hero_image": "/media/hero/tea-hero.jpg",
            "section_title": "Pick your tea favourite.",
            "empty_message": "Our tea counter is being prepared. Please check back soon.",
            "placeholder_icon": "☕",
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
