from rest_framework import serializers

from apps.carts.models import Cart, CartItem
from apps.products.api.serializers.helper import UserSerializer
from apps.products.api.serializers.product import ProductListSerializer


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        exclude = ("cart",)

    def create(self, validated_data):
        cart = Cart.objects.filter(user=self.context["request"].user).first()
        if not cart:
            cart = Cart.objects.create(user=self.context["request"].user)
        validated_data["cart"] = cart
        return super().create(validated_data)


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("quantity",)


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
