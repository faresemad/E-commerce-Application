from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from apps.carts.models import Cart, CartItem
from apps.orders.api.serializers import OrderSerializer
from apps.orders.models import Order


class OrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(user=request.user, cart=cart)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            order.items.add(item)
        order.save()
        cart_items.delete()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
