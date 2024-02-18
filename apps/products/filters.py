from django_filters import rest_framework as filters

from apps.products.models import Product


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "category": ["exact"],
            "price": ["lte", "gte"],
        }
