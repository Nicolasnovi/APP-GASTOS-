from django.urls import path
from .views import crear_usuario, ingreso_gasto

urlpatterns = [
    path('agregar-movimiento/<Fecha>/<Categoria>/<Importe>/<Nota>/<Tipo_movimiento>/', ingreso_gasto),
    path('crear-usuario/<Nombre>/<Apellido>/<Email>/<Contraseña>/', crear_usuario),
]
