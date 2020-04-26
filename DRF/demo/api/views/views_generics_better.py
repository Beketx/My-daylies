from rest_framework import generics
from rest_framework import mixins
from api.models import Category, Product
from api.serializers import CategorySerializer2, ProductSerializer, CategoryWithProductsSerializer
from rest_framework.permissions import IsAuthenticated

class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class  = CategorySerializer2
    permission_classes = (IsAuthenticated,)
    
class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2
    lookup_url_kwarg = 'category_id'

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryWithProductsAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithProductsSerializer