from rest_framework import serializers

from apps.products.models import Category


class CategroyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description"]
        extra_kwargs = {
            "name": {"required": True},
            "description": {"required": False},
        }


class CategroyDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id"]
        extra_kwargs = {
            "id": {"required": True},
        }

    def validate(self, data):
        id = data.get("id")
        if not Category.objects.filter(id=id).exists():
            raise serializers.ValidationError("Category not found")
        elif Category.objects.get(id=id).products.exists():
            raise serializers.ValidationError("Category contains products")
        return data


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "description"]
        read_only_fields = ["name", "slug", "description"]
