from django.db import models

class Piscina(models.Model):
    largo = models.FloatField()  # Largo de la piscina en metros
    ancho = models.FloatField()  # Ancho de la piscina en metros
    profundidad = models.FloatField()  # Profundidad en metros

    def __str__(self):
        return f"Piscina {self.largo}m x {self.ancho}m x {self.profundidad}m"

    @property
    def volumen(self):
        """Calcula el volumen de la piscina en metros cúbicos."""
        return self.largo * self.ancho * self.profundidad