
from rest_framework import serializers

from app.ws.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class CreateImageSerializer(ImageSerializer):
    pass


class RetrieveImageSerializer(ImageSerializer):
    pass
