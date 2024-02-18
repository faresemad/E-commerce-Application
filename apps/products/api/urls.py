from rest_framework.routers import DefaultRouter

from apps.products.api.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()

router.register(r"list", ProductViewSet, basename="products")
router.register(r"categories", CategoryViewSet, basename="categories")

urlpatterns = router.urls
