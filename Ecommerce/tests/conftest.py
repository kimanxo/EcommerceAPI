from pytest_factoryboy import register
from .factories import CategoryFactory, BrandFactory, ProductFactory, ProductLineFactory
from rest_framework.test import APIClient
from pytest import fixture

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)
@fixture
def rest_client():
    return APIClient
