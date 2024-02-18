from rest_framework import mixins, viewsets

from apps.products.api.serializers.product import ProductListSerializer, ProductRetrieveSerializer
from apps.products.models import Product


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductRetrieveSerializer
        return self.serializer_class
