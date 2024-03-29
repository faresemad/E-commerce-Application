from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.carts.api.serializers import (
    CartCreateUpdateSerializer,
    CartItemCreateSerializer,
    CartItemListRetrieveSerializer,
    CartItemUpdateSerializer,
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

    def create(self, request, *args, **kwargs):
        existing_cart = Cart.objects.filter(user=request.user).first()
        if existing_cart:
            return Response({"error": "Cart already exists"}, status=status.HTTP_400_BAD_REQUEST)
        super().create(request, *args, **kwargs)
        return Response({"message": "Cart created successfully"}, status=status.HTTP_201_CREATED)


class CartItemViewSet(
    viewsets.ModelViewSet,
):
    serializer_class = CartItemCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CartItemListRetrieveSerializer
        if self.action == "update":
            return CartItemUpdateSerializer
        return CartItemCreateSerializer

    def create(self, request, *args, **kwargs):
        channel_layer = get_channel_layer()
        super().create(request, *args, **kwargs)
        # Send Notifications
        async_to_sync(channel_layer.group_send)(
            f"notification_{request.user.username}",  # Group name
            {
                "type": "notification_message",
                "message": "Cart item has been created",
                "user": request.user.username,
            },
        )
        return Response({"message": "Cart item created successfully"}, status=status.HTTP_201_CREATED)
