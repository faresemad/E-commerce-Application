from rest_framework import serializers

from apps.products.api.serializers.helper import ProductImageSerializer, ProductReviewSerializer
from apps.products.models import Product, ProductImage


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    upload_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False), write_only=True
    )

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("id", "slug")

    def craete(self, validated_data):
        images = validated_data.pop("upload_images", [])
        product = Product.objects.create(**validated_data)
        for image in images:
            ProductImage.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        images = validated_data.pop("upload_images", [])
        instance = super().update(instance, validated_data)
        for image in images:
            ProductImage.objects.create(product=instance, image=image)
        return instance


class ProductListSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"


class ProductRetrieveSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"
