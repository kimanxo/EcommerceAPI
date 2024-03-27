from rest_framework.pagination import PageNumberPagination


class ProductPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page"
    max_page_size = 1000


class BrandPaginator(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page"
    max_page_size = 1000


class CategoryPaginator(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page"
    max_page_size = 1000
