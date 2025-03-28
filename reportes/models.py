from django.db import models

class Equipo(models.Model):
    TIPOS_EQUIPO = (
        ('PC', 'Computadora'),
        ('MOUSE', 'Mouse'),
        ('TECLADO', 'Teclado'),
        ('OTRO', 'Otro'),
    )
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_EQUIPO)
    descripcion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=100, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class ReporteDanio(models.Model):
    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('REPARADO', 'Reparado'),
        ('BAJA', 'Dado de Baja'),
    )
    
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    descripcion_danio = models.TextField()
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')

    def __str__(self):
        return f"Reporte {self.id} - {self.equipo.nombre}"