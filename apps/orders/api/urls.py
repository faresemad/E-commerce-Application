from rest_framework.routers import DefaultRouter

from apps.orders.api.views import OrdersHistoryViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"orders-history", OrdersHistoryViewSet, basename="orders-history")
router.register(r"orders", OrderViewSet, basename="order")
urlpatterns = router.urls
