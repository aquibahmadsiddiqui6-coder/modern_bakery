from django.contrib import admin
from .models import Product, ProductImage, HomepageMedia


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(HomepageMedia)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "is_available",
        "created_at",
    )

    list_filter = (
        "category",
        "is_available",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "-created_at",
    )
