import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:

    endpoint = "/api/category/"

    def test_category_get_request(self, category_factory, rest_client):

        category_factory.create_batch(7)
        response = rest_client().get(self.endpoint)
        assert response.status_code == 200
        response_data = json.loads(response.content)
        assert len(response_data["results"]) == 7


class TestBrandEndpoints:

    endpoint = "/api/brand/"

    def test_brand_get_request(self, brand_factory, rest_client):

        brand_factory.create_batch(7)
        response = rest_client().get(self.endpoint)
        assert response.status_code == 200
        response_data = json.loads(response.content)
        assert len(response_data["results"]) == 7


class TestProductEndpoints:

    endpoint = "/api/product/"

    def test_product_get_all_products(self, product_factory, rest_client):

        product_factory.create_batch(1)
        response = rest_client().get(self.endpoint)
        assert response.status_code == 200
        response_data = json.loads(response.content)
        assert len(response_data["results"]) == 1

    def test_get_single_product_by_name(self, product_factory, rest_client):
        obj = product_factory(slug="slug-test")
        response = rest_client().get(f"{self.endpoint}{obj.slug}/")
        assert len(json.loads(response.content)) == 1
        

    def test_get_single_category_by_name(self, product_factory, rest_client):
        pass
