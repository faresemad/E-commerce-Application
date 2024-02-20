from rest_framework.routers import DefaultRouter

from apps.carts.api.views import CartViewSet

router = DefaultRouter()
router.register(r"carts", CartViewSet, basename="carts")
urlpatterns = router.urls
