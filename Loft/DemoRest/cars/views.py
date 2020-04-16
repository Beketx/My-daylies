from django.shortcuts import render
from cars.models import Car
from cars.serializers import CarDetailSerializer
from rest_framework import generics

# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
