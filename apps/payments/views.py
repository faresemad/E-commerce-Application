from decimal import Decimal

import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.orders.models import Order
from apps.payments.serializers import PaymentSerializer

# create the Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


class PaymentViewSet(viewsets.ViewSet):
    def get_serializer_class(self):
        if self.action == "process_payment":
            return PaymentSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=["post"])
    def process_payment(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_id = serializer.validated_data["order_id"]
        order = get_object_or_404(Order, id=order_id)

        success_url = request.build_absolute_uri(reverse("payment:completed"))
        cancel_url = request.build_absolute_uri(reverse("payment:canceled"))
        # Stripe checkout session data
        session_data = {
            "mode": "payment",
            "client_reference_id": order.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": [],
        }
        # add order items to the Stripe checkout session
        for item in order.items.all():
            session_data["line_items"].append(
                {
                    "price_data": {
                        "unit_amount": int(item.price * Decimal("100")),
                        "currency": "usd",
                        "product_data": {
                            "name": item.product.name,
                        },
                    },
                    "quantity": item.quantity,
                }
            )
        # Check if any line items were added
        if not session_data["line_items"]:
            return Response("No items to process", status=status.HTTP_400_BAD_REQUEST)
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        return Response({"url": session.url})


def payment_completed(request):
    return render(request, "payment/completed.html")


def payment_canceled(request):
    return render(request, "payment/canceled.html")
