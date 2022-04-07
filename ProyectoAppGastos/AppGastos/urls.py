from django.urls import path
from .views import dashboard, ingreso_gasto, inicio
from .views import crear_usuario, ingreso_gasto

urlpatterns = [
    path('agregar-movimiento/<Fecha>/<Categoria>/<Importe>/<Nota>/<Tipo_movimiento>/',ingreso_gasto),
    path('',inicio),
    path('crear-usuario/<Nombre>/<Apellido>/<Email>/<Contraseña>/', crear_usuario),
    path('Dashboard/',dashboard)

]
