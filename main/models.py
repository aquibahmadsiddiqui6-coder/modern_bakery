from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ("cakes", "Cakes"),
        ("pastries", "Pastries"),
        ("pancakes", "Pancakes"),
        ("biscuits", "Biscuits & Cookies"),
        ("sandwiches", "Sandwiches"),
        ("snacks", "Bakery Snacks"),
        ("namkeen", "Namkeen"),
        ("beverages", "Tea & Beverages"),
    ]

    name = models.CharField(max_length=150)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(upload_to="products/gallery/")

    alt_text = models.CharField(max_length=150, blank=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("display_order", "id")

    def __str__(self):
        return f"{self.product.name} image {self.pk}"


class HomepageMedia(models.Model):

    MEDIA_TYPE_CHOICES = [
        ("photo", "Photo"),
        ("video", "Video"),
    ]

    SECTION_CHOICES = [
        ("shop", "Our Shop"),
        ("products", "Our Products"),
        ("behind", "Behind the Bakery"),
        ("cakes", "Cake Gallery"),
    ]

    title = models.CharField(max_length=150)

    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES
    )

    section = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES
    )

    image = models.ImageField(
        upload_to="homepage/photos/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="homepage/videos/",
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
