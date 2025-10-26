from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Product
from .serializers import ProductSerializer
from webstore.mixins.pagination import OptionalPaginationMixin

# Create your views here.
class ProductViewSet(OptionalPaginationMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name']
    filterset_fields = {
        'name': ['exact', 'icontains'],
        'description': ['exact', 'icontains'],
        'price': ['exact', 'icontains'],
        'stock': ['exact', 'icontains'],
    }
    ordering_fields = ['name']