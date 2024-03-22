from itertools import product
from rest_framework.serializers import ModelSerializer
from .models import Category, Brand, Product, ProductLine
from rest_framework import serializers


class CategorySerializer(ModelSerializer):

    class Meta:

        model = Category
        fields = ["name", "id", "created_at"]


class BrandSerializer(ModelSerializer):

    class Meta:

        model = Brand
        fields = "__all__"


class ProductLineSerializer(ModelSerializer):

    parent_product_name = serializers.CharField(source="product.name")
    parent_product_id = serializers.IntegerField(source="product.pk")

    class Meta:

        model = ProductLine
        fields = [
            "price",
            "sku",
            "stock_qty",
            "is_active",
            "parent_product_name",
            "parent_product_id",
        ]


class ProductSerializer(ModelSerializer):

    brand = BrandSerializer()
    category = CategorySerializer()
    product_line = ProductLineSerializer(many=True)

    class Meta:

        model = Product
        fields = "__all__"
