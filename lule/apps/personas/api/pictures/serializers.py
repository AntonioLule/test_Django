from rest_framework import serializers

# Models
from apps.personas.models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'
        read_only_field = ('owner',)


class PhotoListSerializer(PhotoSerializer):

    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')  # Para el listado solo quiero regresar esos campos