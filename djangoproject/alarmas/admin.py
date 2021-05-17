from django.contrib import admin
from .models import Alarma

class AlarmaAdmin(admin.ModelAdmin):    
    list_display =["idAlarma", "estadoAlarma"]
    search_fields=["idAlarma"]


admin.site.register(Alarma, AlarmaAdmin)
# Register your models here.
