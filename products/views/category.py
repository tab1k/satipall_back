from rest_framework import viewsets

from products.models import ProductCategory
from products.filters import ProductCategoryFilterSet
from products.serializers import ProductCategoryShortSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryShortSerializer
    filterset_class = ProductCategoryFilterSet
