from rest_framework import serializers
from .models import Proyecto, TipoNota, Nota

class TipoNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNota
        fields = '__all__'

class NotaSerializer(serializers.ModelSerializer):
    tipo_nombre = serializers.ReadOnlyField(source='tipo.nombre')

    class Meta:
        model = Nota
        fields = ['id', 'titulo', 'contenido', 'proyecto', 'tipo', 'tipo_nombre', 'creado_en']

class ProyectoSerializer(serializers.ModelSerializer):
    # Campo calculado para devolver el conteo de notas del proyecto
    total_notas = serializers.SerializerMethodField()

    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'descripcion', 'usuario', 'total_notas', 'creado_en']

    def get_total_notas(self, obj):
        return obj.notas.count()