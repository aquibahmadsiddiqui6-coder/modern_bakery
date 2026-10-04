def cart(request):
    items = request.session.get("cart", {})
    return {
        "cart_count": sum(int(quantity) for quantity in items.values()),
    }
