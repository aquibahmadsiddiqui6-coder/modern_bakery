from django.contrib import admin
from .models import Product, ProductImage, HomepageMedia, Order, OrderItem


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(HomepageMedia)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_name", "unit_price", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "phone", "total", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer_name", "phone", "email")
    inlines = (OrderItemInline,)
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
