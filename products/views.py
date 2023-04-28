from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import ProductCategory, Maker, Product

from products.serializers import (
    ProductCategorySerializer,
    MakerSerializer,
    ProductSerializer,
)


class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class MakerListView(ListAPIView):
    serializer_class = MakerSerializer
    queryset = Maker.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
