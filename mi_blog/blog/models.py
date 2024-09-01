from django.db import models
#Definir modelo "Publicacion"
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return str(self.titulo)
