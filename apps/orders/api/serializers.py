from rest_framework import serializers

from apps.orders.models import Order, OrderItem
from apps.products.api.serializers.helper import UserSerializer
from apps.products.api.serializers.product import ProductListSerializer


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ("id", "user")


class OrderItemListRetrieveSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()
    order = serializers.StringRelatedField()
    product = ProductListSerializer()

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "quantity", "price", "cost")

    def get_cost(self, obj: OrderItem):
        return obj.get_cost()


class OrderListRetrieveSerializer(serializers.ModelSerializer):
    items = OrderItemListRetrieveSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "user", "items", "created_at", "updated_at", "total_cost")

    def get_total_cost(self, obj: Order):
        return obj.get_total_cost()
