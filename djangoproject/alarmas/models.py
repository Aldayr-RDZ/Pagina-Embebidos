from django.db import models

# Create your models here.
class Alarma(models.Model):
    idAlarma = models.UUIDField(primary_key = True)
    estadoAlarma = models.BooleanField()

    def __str__(self):
        return str(self.idAlarma)
    