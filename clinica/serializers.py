from rest_framework import serializers
from .models import Propietario, Mascota, ConsultaVeterinaria


class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

    def validate_peso(self, value):
        if value <= 0:
            raise serializers.ValidationError("El peso debe ser mayor que 0.")
        return value

    def validate_nombre(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la mascota no puede estar vacío.")
        return value


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaVeterinaria
        fields = '__all__'

    def validate_costo(self, value):
        if value < 0:
            raise serializers.ValidationError("El costo no puede ser negativo.")
        return value

    def validate_motivo(self, value):
        if not value:
            raise serializers.ValidationError("El motivo de la consulta no puede estar vacío.")
        return value