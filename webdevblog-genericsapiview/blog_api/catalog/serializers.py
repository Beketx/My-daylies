from rest_framework import serializers
from catalog.models import Ball
class BallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ball
        fields = ['title','size', 'player_id']

    # title = serializers.CharField(max_length=120)
    # size = serializers.IntegerField()
    # player_id = serializers.IntegerField()