from django.contrib import admin
from .models import Brand, Category, Product, ProductLine


# creating a tabular inline  for the product line
class ProductLineInline(admin.TabularInline):
    model = ProductLine


# registering the ProductLine TabularInline to the product model in the admin panel


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


# registering models
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductLine)
