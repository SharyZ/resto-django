from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = ['id', 'name', 'image',
                  'small_description', 'price', 'category']
