from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, RegisterView

router = DefaultRouter()
router.register("notas", NotaViewSet, basename="nota")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
] + router.urls