from django.urls import path
from .views import crear_usuario, ingreso_gasto, objetivos

urlpatterns = [
     path('objetivos/<Objetivo>/<MontoDelObjetivo>/<Fecha>/<Observacion>/', objetivos),

    path('agregar-movimiento/<Fecha>/<Categoria>/<Importe>/<Nota>/<Tipo_movimiento>/', ingreso_gasto),

    path('crear-usuario/<Nombre>/<Apellido>/<Email>/<Contraseña>/', crear_usuario),
]
