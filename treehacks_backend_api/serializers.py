from rest_framework import serializers
from .models import Photo, PhotoResponse

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["imgUrl"]

class ResponseSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):
        model = PhotoResponse
        fields = ["status", "name", "imgUrl", "location"]
