from rest_framework import serializers
from .models import Nota
from django.contrib.auth.models import User


class NotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nota
        fields = "__all__"
        read_only_fields = ["usuario", "fecha_creacion", "fecha_actualizacion"]


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def create(self, validated_data):
        usuario = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"]
        )

        return usuario