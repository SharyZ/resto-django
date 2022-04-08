from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'products']
