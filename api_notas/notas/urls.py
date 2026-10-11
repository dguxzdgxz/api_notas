from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet, TipoNotaViewSet, NotaViewSet

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet, basename='proyecto')
router.register(r'tipos', TipoNotaViewSet, basename='tiponota')
router.register(r'notas', NotaViewSet, basename='nota')

urlpatterns = [
    path('', include(router.urls)),
]