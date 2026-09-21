from django.contrib import admin
from .models import Propietario, Mascota, ConsultaVeterinaria

admin.site.register(Propietario)
admin.site.register(Mascota)
admin.site.register(ConsultaVeterinaria)