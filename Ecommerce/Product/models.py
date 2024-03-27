from enum import unique
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class ActiveManager(models.Manager):
    def active(self):
        return super().get_queryset().filter(is_active=True)


class Category(MPTTModel):

    name = models.CharField(
        max_length=64, blank=False, null=False, unique=True, help_text="Category name"
    )
    parent = TreeForeignKey("self", on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(
        max_length=64, blank=True, null=False, unique=True, help_text="Brand name"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]


class Product(models.Model):

    name = models.CharField(
        max_length=256, blank=False, null=False, unique=False, help_text="Product name"
    )
    slug = models.SlugField(
        max_length=256, blank=False, null=False, unique=True, help_text="Product slug"
    )

    description = models.TextField(
        max_length=1024,
        blank=False,
        null=False,
        unique=False,
        help_text="Product description",
    )

    is_digital = models.BooleanField(
        default=False, help_text="is the product digital ?"
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Product brand",
    )

    category = TreeForeignKey(
        "Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Product category",
    )
    is_active = models.BooleanField(default=False, help_text="is the product active")

    objects = ActiveManager()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]


class ProductLine(models.Model):

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        help_text="Product price",
    )
    sku = models.CharField(
        max_length=128, blank=False, null=False, help_text="Product SKU"
    )
    stock_qty = models.IntegerField(
        blank=False, null=False, help_text="Product quantity in stock"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        help_text="Related product",
        related_name="product_line",
    )
    is_active = models.BooleanField(default=False, help_text="is the product active")
    objects = ActiveManager()
    order = models.PositiveIntegerField(
        unique=True, blank=False, null=False, help_text="product line order"
    )
    created_at = models.DateTimeField(auto_now_add=True)
