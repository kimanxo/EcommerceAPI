from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(
        max_length=64, blank=True, null=False, unique=True, help_text="Brand name"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length=256, blank=False, null=False, unique=False, help_text="Product name"
    )

    description = models.TextField(
        max_length=1024,
        blank=False,
        null=False,
        unique=False,
        help_text="Product description",
    )

    is_digital = models.BooleanField(default=False)
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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
