from django.urls import path
from .views import ingreso_gasto

urlpatterns = [
    path('agregar-movimiento/<Fecha>/<Categoria>/<Importe>/<Nota>/<Tipo_movimiento>/',ingreso_gasto),
]
