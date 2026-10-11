from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class TipoNota(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Tarea, Bug, Idea, Recordatorio

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='notas', null=True, blank=True)
    tipo = models.ForeignKey(TipoNota, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo