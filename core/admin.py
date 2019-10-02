from django.contrib import admin
from .models import (
    Marca,
     Veiculo,
      Pessoa,
       Paramentros,
        MovRotativo,
         Mensalista,
          MovMensalista,
        )

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin','checkout','valor_hora', 'pago', 'total', 'horas_total', 
        'veiculo' )

    def veiculo(self,obj):
           return obj.veiculo

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista','dt_pgto','total',)         

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Paramentros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)

