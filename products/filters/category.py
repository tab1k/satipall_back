import django_filters

from products.models import ProductCategory


class ProductCategoryFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ProductCategory
        fields = (
            "id",
            "name",
        )
