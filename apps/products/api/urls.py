from rest_framework.routers import DefaultRouter

from apps.products.api.views import ProductViewSet

router = DefaultRouter()

router.register(r"list", ProductViewSet, basename="products")

urlpatterns = router.urls
