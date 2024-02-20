from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.carts.api.serializers import (
    CartCreateUpdateSerializer,
    CartItemCreateUpdateSerializer,
    CartItemListRetrieveSerializer,
    CartListRetrieveSerializer,
)
from apps.carts.models import Cart, CartItem


class CartViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CartCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CartListRetrieveSerializer
        return CartCreateUpdateSerializer


class CartItemViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CartItemCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CartItemListRetrieveSerializer
        return CartItemCreateUpdateSerializer
