from rest_framework.serializers import ModelSerializer
from .models import Category, Brand, Product, ProductImage, ProductLine
from rest_framework import serializers


class CategorySerializer(ModelSerializer):

    class Meta:

        model = Category
        fields = ["name", "id", "created_at"]


class BrandSerializer(ModelSerializer):

    class Meta:

        model = Brand
        fields = "__all__"


class ProductImageSerializer(ModelSerializer):

    class Meta:
        model = ProductImage
        exclude = ("id",)

class ProductLineSerializer(ModelSerializer):
    product_image   = ProductImageSerializer(many=True)
    # serializing the parent product name and id to output a verbose name instead of IDs or PKs
    parent_product_name = serializers.CharField(source="product.name")
    parent_product_id = serializers.IntegerField(source="product.pk")

    class Meta:

        model = ProductLine
        fields = [
            "price",
            "sku",
            "stock_qty",
            "is_active",
            "order",
            "product_image",
            "parent_product_name",
            "parent_product_id",
        ]


class ProductSerializer(ModelSerializer):
    # utilizing nested serializers to fully serialize the product with all its relevant infos 
    brand = BrandSerializer()
    category = CategorySerializer()
    product_line = ProductLineSerializer(many=True)

    class Meta:

        model = Product
        fields = "__all__"
