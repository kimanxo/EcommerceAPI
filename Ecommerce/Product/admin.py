from django.contrib import admin
from django.urls import reverse
from .models import (
    AttributeValue,
    Brand,
    Category,
    Product,
    ProductImage,
    ProductLine,
    Attribute,
)
from django.utils.safestring import mark_safe


# creating a tabular inline  for the product line
class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )
        if instance.pk:
            link = mark_safe(f"<a href ='{url}'>Edit<a/>")
            return link
        else:
            return ""


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue.product_line_attr_value.through


class ProductLineImageInline(admin.TabularInline):
    model = ProductImage


# registering the ProductLine TabularInline to the product model in the admin panel


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductLineImageInline, AttributeValueInline]


# registering models
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(AttributeValue)
admin.site.register(Attribute)

# admin.site.register(ProductLine)
