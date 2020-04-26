from rest_framework import serializers

from api.models import Category, Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'))
        return category

    def update(self, instance, validated_data):
        # instance.name = validated_data.get('name', instance.name)
        # instance.id = validated_data.get('id')
        instance = validated_data 
        instance.save()
        return instance

class CategorySerializer2(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=2000) its overriding the name from models
    class Meta:
        model = Category
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer2(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ['id','name','price','description','category','category_id']

class CategoryWithProductsSerializer(serializers.ModelSerializer):
    produkt = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','produkt']