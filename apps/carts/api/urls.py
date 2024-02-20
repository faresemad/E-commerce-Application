from rest_framework.routers import DefaultRouter

from apps.carts.api.views import CartItemViewSet, CartViewSet

router = DefaultRouter()
router.register(r"carts", CartViewSet, basename="carts")
router.register(r"cart-items", CartItemViewSet, basename="cart-items")
urlpatterns = router.urls
