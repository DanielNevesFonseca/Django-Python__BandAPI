from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'album_id']
        read_only_fields = ['id', 'album_id']

    album_id = serializers.SerializerMethodField("get_album_id")

    def get_album_id(self, song: Song):
        return song.album.id

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
