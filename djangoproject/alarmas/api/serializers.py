from rest_framework import serializers
from alarmas.models import Alarma

class AlarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarma
        fields = ['idAlarma','estadoAlarma']