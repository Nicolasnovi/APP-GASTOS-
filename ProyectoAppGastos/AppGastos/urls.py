from django.urls import path
from .views import ingreso_gasto, inicio, crear_usuario, movimientos_form, usuario_form

urlpatterns = [
    path('',inicio),
    path('agregar-movimiento/<Fecha>/<Categoria>/<Importe>/<Nota>/<Tipo_movimiento>/',ingreso_gasto),
    path('crear-usuario/<Nombre>/<Apellido>/<Email>/<Contraseña>/', crear_usuario),
    path('usuarioFormulario/', usuario_form),
    path('movimientosFormulario/', movimientos_form),
]
