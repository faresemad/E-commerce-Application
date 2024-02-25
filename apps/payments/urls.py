from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.payments import views, webhooks

app_name = "payment"

router = DefaultRouter()
router.register(r"payment", views.PaymentViewSet, basename="process")

urlpatterns = [
    path("completed/", views.payment_completed, name="completed"),
    path("canceled/", views.payment_canceled, name="canceled"),
    path("webhooks/", webhooks.stripe_webhook, name="webhooks"),
    path("", include(router.urls)),
]
