from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=slug)
        serializer = CategorySerializer(category)

        return Response(serializer.data)
