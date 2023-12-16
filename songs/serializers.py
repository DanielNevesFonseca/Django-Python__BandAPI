from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['id', 'album_id']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
