from rest_framework import serializers

from apps.carts.models import Cart, CartItem
from apps.products.api.serializers.helper import UserSerializer
from apps.products.api.serializers.product import ProductListSerializer


class CartItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartItemListRetrieveSerializer(serializers.ModelSerializer):
    cart = serializers.StringRelatedField()
    product = ProductListSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"


class CartCreateUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = "__all__"


class CartListRetrieveSerializer(serializers.ModelSerializer):
    items = CartItemListRetrieveSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Cart
        fields = "__all__"
