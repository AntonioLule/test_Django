from rest_framework import serializers

# Models
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        Crea una instancia de User a partir de los datos validated_data que contiene valores deserealizados
        :param validated_data: Diccionario con datos de usuario
        :return: objeto user
        """

        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de del usuario a partir del validate data
        :param instance: Objetop user a actualizar
        :param validated_data: diccionario con nuevos valores
        :return: objeto user
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data
