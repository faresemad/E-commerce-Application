from rest_framework import serializers

from apps.products.api.serializers.helper import UserSerializer
from apps.products.models import ProductReview


class ProductReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ["product", "review", "rating"]

    def create(self, validated_data):
        user = self.context["request"].user
        review = ProductReview.objects.create(user=user, **validated_data)
        return review


class ProductReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ProductReview
        fields = ["user", "review", "rating"]
