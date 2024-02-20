from django.db import transaction
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from apps.carts.models import Cart, CartItem
from apps.orders.api.serializers import OrderSerializer
from apps.orders.models import Order, OrderItem


class OrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        with transaction.atomic():
            order = Order.objects.create(user=request.user, cart=cart)
            cart_items = CartItem.objects.filter(cart=cart)
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order, product=cart_item.product, quantity=cart_item.quantity, price=cart_item.product.price
                )
            order.save()
            cart_items.delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
