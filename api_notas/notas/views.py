from rest_framework import viewsets, permissions
from .models import Proyecto, TipoNota, Nota
from .serializers import ProyectoSerializer, TipoNotaSerializer, NotaSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # El usuario solo ve sus propios proyectos
        return Proyecto.objects.filter(usuario=self.request.user)

class TipoNotaViewSet(viewsets.ModelViewSet):
    queryset = TipoNota.objects.all()
    serializer_class = TipoNotaSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotaViewSet(viewsets.ModelViewSet):
    serializer_class = NotaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Nota.objects.filter(proyecto__usuario=self.request.user)
        
        # Filtrado por tipo desde URL (?tipo=1)
        tipo_id = self.request.query_params.get('tipo')
        if tipo_id:
            queryset = queryset.filter(tipo_id=tipo_id)
            
        # Filtrado por proyecto desde URL (?proyecto=2)
        proyecto_id = self.request.query_params.get('proyecto')
        if proyecto_id:
            queryset = queryset.filter(proyecto_id=proyecto_id)

        return queryset