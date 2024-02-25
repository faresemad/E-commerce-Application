from django.db import transaction
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.carts.models import Cart, CartItem
from apps.orders.api.serializers import OrderCreateSerializer, OrderListRetrieveSerializer
from apps.orders.models import Order, OrderItem


class OrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        with transaction.atomic():
            order = Order.objects.create(
                user=request.user,
                cart=cart,
                address=request.data["address"],
                postal_code=request.data["postal_code"],
                city=request.data["city"],
            )
            cart_items = CartItem.objects.filter(cart=cart)
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order, product=cart_item.product, quantity=cart_item.quantity, price=cart_item.product.price
                )
            order.save()
            cart_items.delete()
            # Store the UUID in the session
            request.session["order_id"] = str(order.id)
        return Response({"id": order.id}, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderListRetrieveSerializer
        return self.serializer_class
