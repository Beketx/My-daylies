from rest_framework import serializers 
from publisher.models import Author,Book
class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    surname = serializers.CharField(max_length=120)
    age = serializers.IntegerField()
    def create(self,validated_data):
        return Author.objects.create(**validated_data)
