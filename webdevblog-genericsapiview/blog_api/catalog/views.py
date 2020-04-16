from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response


from catalog.serializers import BallSerializer
from catalog.models import *
# from rest_framework.response import Response

class BallViewSet(viewsets.ModelViewSet):
    queryset = Ball.objects.all()
    serializer_class = BallSerializer
    # def list(self,request):
    #     queryset = Ball.objects.all()
    #     serializer = BallSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self,request , pk=None):
    #     queryset = Ball.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = BallSerializer(user)
    #     return Response(serializer.data)