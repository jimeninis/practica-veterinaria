from django.db import models

class Propietario(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.CASCADE,
        related_name='mascotas'
    )
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class ConsultaVeterinaria(models.Model):
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField(max_length=200)
    diagnostico = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    costo = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Consulta de {self.mascota.nombre} el {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"