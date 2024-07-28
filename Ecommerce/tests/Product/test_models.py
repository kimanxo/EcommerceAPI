import pytest
from Ecommerce.Product.models import Product

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        instance = category_factory()
        assert instance.__str__().startswith("Category_")


class TestBrandModel:

    def test_str_method(self, brand_factory):
        instance = brand_factory()
        assert instance.__str__().startswith("Brand_")


class TestProductModel:

    def test_str_method(self, product_factory):
        instance = product_factory()
        assert instance.__str__().startswith("Product_")
        assert instance.description == "dummy product description"
        assert instance.is_digital
        assert instance.is_active


class TestProductLineModel:

    def test_str_method(self, product_line_factory):
        instance = product_line_factory()
        assert instance.price == 100
        assert instance.sku == "E313"
        assert instance.stock_qty == 300
        assert instance.is_active



