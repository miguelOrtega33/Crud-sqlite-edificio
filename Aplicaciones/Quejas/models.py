from django.db import models

class Usuario(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    mensaje=models.CharField(max_length=500)
    piso= models.PositiveIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.mensaje, self.piso)
