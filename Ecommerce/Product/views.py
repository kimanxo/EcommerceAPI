from rest_framework.viewsets import ViewSet
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action


@extend_schema(responses=CategorySerializer)
class CategoryViewSet(ViewSet):

    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(responses=BrandSerializer)
class BrandViewSet(ViewSet):

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(responses=ProductSerializer)
class ProductViewSet(ViewSet):

    queryset = Product.objects.active()
    lookup_field = "slug"

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category>\w+)/all",
        url_name="product_by_category",
    )
    def list_products_by_category(self, request, category=None):
        serializer = ProductSerializer(
            self.queryset.filter(category__name=category), many=True
        )
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug), many=True)
        return Response(serializer.data)
