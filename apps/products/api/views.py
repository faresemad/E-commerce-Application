from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from apps.products.api.serializers.category import CategoryListSerializer
from apps.products.api.serializers.product import ProductListSerializer, ProductRetrieveSerializer
from apps.products.filters import ProductFilter
from apps.products.models import Category, Product


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ["name", "category__name"]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductRetrieveSerializer
        return self.serializer_class


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = "slug"
