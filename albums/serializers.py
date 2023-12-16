from rest_framework import serializers
from users.models import User

from users.serializers import UserSerializer
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'user']
        depth = 1
        read_only_fields = ['user']
    
    user = UserSerializer(read_only=True)

    

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
