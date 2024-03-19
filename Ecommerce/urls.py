from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from Ecommerce.Product import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = DefaultRouter()

router.register(r"category", views.CategoryViewSet)
router.register(r"brand", views.BrandViewSet)
router.register(r"product", views.ProductViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
