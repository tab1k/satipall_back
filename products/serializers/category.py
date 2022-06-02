from rest_framework import serializers

from products.models import ProductCategory


class ProductCategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            "name",
        )
