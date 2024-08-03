from os import name
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField

# creating  a custom manager to filter out the active product lines .


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
    # overriding the default manager with the custom manager
    objects = ActiveManager()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    attr_value = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute,related_name="attribute_value", help_text="attribute", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.attribute} - {self.attr_value}"


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

    order = OrderField(
        unique_for_field="product",
        blank=True,
        help_text="product line order",
    )
    attr_value = models.ManyToManyField(AttributeValue,through="ProductLineAttributeValue", related_name="product_line_attr_value")
    # overriding the default manager with the custom manager
    objects = ActiveManager()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ProductLineAttributeValue(models.Model):
    attr_value = models.ForeignKey(
        AttributeValue,
        related_name="attribute_value",
        help_text="attribute",
        on_delete=models.CASCADE,
    )
    product_line = models.ForeignKey(
        ProductLine,
        related_name="attr_product_line",
        help_text="product line",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("attr_value", "product_line")


class ProductImage(models.Model):
    
    alt_text = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        unique=False,
        help_text="Product image alt",
    )
    url = models.ImageField(upload_to=None,)
    product_line = models.ForeignKey(
        ProductLine,
        on_delete=models.CASCADE,
        help_text="Related product",
        related_name="product_image",
        default="img.jpg"
    )
    order = OrderField(unique_for_field="product_line", blank=True)

    def __str__(self):
        return self.alt_text
