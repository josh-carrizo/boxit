from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Reserva

# Create your views here.

def reporte_mensual(request):
    resumen = Reserva.objects.values('box__nombre')\
        .annotate(uso_horas=Sum('hora_fin') - Sum('hora_inicio'))
    return render(request, 'gestion_box/reporte.html', {'resumen': resumen})
