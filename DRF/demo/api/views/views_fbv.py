import json
from django.http.response import JsonResponse
from api.models import Category,Product
from api.serializers import CategorySerializer,CategorySerializer2
from rest_framework.decorators import api_view 
from rest_framework.request import Request
from rest_framework.response import Response  
from rest_framework import status

@api_view(['GET','POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer2
        return Response(serializer.data, status=)
    elif request.method == 'POST':
        serializer = CategorySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=500)


@api_view(['GET','PUT','DELETE'])
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CategorySerializer2(category)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CategorySerializer2(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    if request.method == 'DELETE':
        category.delete()
        return Response({'delete':True})

# def category_products(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)
#     except Category.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})

#     products = category.products.all()
#     products_json = [p.to_json() for p in products]

#     return JsonResponse(products_json, safe=False)
