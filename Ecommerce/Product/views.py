from rest_framework.viewsets import ModelViewSet
from Ecommerce.utils.paginators import (
    BrandPaginator,
    CategoryPaginator,
    ProductPaginator,
)
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # overriding the list method to implement pagination
    def list(self, request):
        paginator = CategoryPaginator()
        paginated_products = paginator.paginate_queryset(self.queryset, request=request)
        serializer = CategorySerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)


class BrandViewSet(ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    # overriding the list method to implement pagination
    def list(self, request):
        paginator = BrandPaginator()
        paginated_products = paginator.paginate_queryset(self.queryset, request=request)
        serializer = BrandSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.active()
    lookup_field = "slug"
    serializer_class = ProductSerializer

    # overriding the list method to implement pagination
    def list(self, request):
        paginator = ProductPaginator()
        paginated_products = paginator.paginate_queryset(self.queryset, request=request)
        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category>\w+)/all",
        url_name="product_by_category",
    )
    # custom method to list products by category
    def list_products_by_category(self, request, category=None):
        paginator = ProductPaginator()
        paginated_products = paginator.paginate_queryset(
            self.queryset.filter(category__name=category), request=request
        )
        serializer = ProductSerializer(paginated_products, many=True)

        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug), many=True)
        return Response(serializer.data)
