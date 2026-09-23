from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Nota
from .serializers import NotaSerializer, RegisterSerializer


class NotaViewSet(viewsets.ModelViewSet):
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        notas = Nota.objects.filter(usuario=self.request.user)

        buscar = self.request.query_params.get("buscar")

        if buscar:
            notas = notas.filter(
                titulo__icontains=buscar
            ) | notas.filter(
                contenido__icontains=buscar
            )

        return notas.order_by("-fecha_creacion")

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @action(detail=False, methods=["get"])
    def estadisticas(self, request):
        cantidad = Nota.objects.filter(usuario=request.user).count()

        return Response({
            "total_notas": cantidad
        })


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"mensaje": "Usuario creado correctamente"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )