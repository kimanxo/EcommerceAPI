import factory
from Ecommerce.Product.models import Category, Product, Brand, ProductLine, ProductImage


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(
        lambda x: "Category_%d" % x,
    )


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(
        lambda x: "Brand_%d" % x,
    )


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(
        lambda x: "Product_%d" % x,
    )

    description = "dummy product description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_active = True


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = 100
    sku = "E313"
    stock_qty = 300
    product = factory.SubFactory(ProductFactory)
    is_active = True


