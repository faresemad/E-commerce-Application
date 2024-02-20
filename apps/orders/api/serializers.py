from rest_framework import serializers

# from apps.carts.api.serializers import CartItemSerializer, CartSerializer
# from apps.carts.models import Cart, CartItem
from apps.orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "quantity", "price", "cost")

    def get_cost(self, obj: OrderItem):
        return obj.get_cost()


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("id", "user", "items", "created_at", "updated_at", "total_cost")

    def get_total_cost(self, obj: Order):
        return obj.get_total_cost()
