from rest_framework import serializers
from images.models import Images


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('id', 'image', 'media_url')


# class ImageUploadSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Images
