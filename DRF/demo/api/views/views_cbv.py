from api.models import Category,Product
from api.serializers import CategorySerializer,CategorySerializer2
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response  
from rest_framework import status

class CategoryListAPIView(APIView):
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer2(category, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CategorySerializer2(data=request.data)
        if seraializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
class CategoryDetailAPIView(APIView):
    def get_object(self,id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist as e:
            return Response({'error':str(e)})
    def get(self,request,category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer2(category)
        return Response(serializer.data)
    def put(self,request,category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer2(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors':serializer.errors})
    def delete(self,request,category_id):
        category = self.get_object(category_id)
        category.delete()
        return Response({'deleted':True})

# def category_products(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)
#     except Category.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})

#     products = category.products.all()
#     products_json = [p.to_json() for p in products]

#     return JsonResponse(products_json, safe=False)
