#so this is a implement of APIView
'''
from rest_framework import serializers 
from delivery.models import *
class ConsumerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    age = serializers.IntegerField()
    food = serializers.CharField(max_length=40)

    def create(self,validated_data):
        consumer = Consumer.objects.create(name=validated_data.get('name'))
        return consumer
        # return Consumer.objects.create(**validated_data)
    def update(self,instance, validated_data):
        instance.name = validated_data.get('name')
        instance.age = validated_data.get('age')
        instance.food = validated_data.get('food')
        instance.save()
        return instance
'''

#so here we use instead MODELSerializer

from rest_framework import serializers

from .models import Consumer

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ['name','age','food']