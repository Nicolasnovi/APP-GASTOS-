from django.http import HttpResponse
from django.shortcuts import render
from .models import movimientos, usuario, objetivo
from django.http import response

# Create your views here.

def objetivos(request,Objetivo,MontoDelObjetivo,Fecha,Observacion):

    nuevo_objetivo = objetivo(
        Objetivo = Objetivo,
        MontoDelObjetivo = MontoDelObjetivo,
        Fecha= Fecha, Observacion= Observacion
        )
    nuevo_objetivo.save()

    return HttpResponse('Objetivo creado con éxito!')

     

def ingreso_gasto(request,Fecha,Categoria,Importe,Nota,Tipo_movimiento):
    #puse un while para que cada vez que se ingrese alguna palabra en vez de un numero tire un error y te vuelva a pedir un numero 
    while True:
        try:  
            mov= movimientos(Fecha=Fecha,Categoria=Categoria,Importe=Importe,Nota=Nota,Tipo_movimiento=Tipo_movimiento)
            mov.save()
            #como me tiraba el error de que no puedo comparar un string con un int , tuve que convertirlo 
            mov_1=int(mov.Importe)
            break
        except:
            return HttpResponse (f'Error, Por favor ingrese un numero en la seccion importe')
    #Logica para diferenciar entre ingreso y gasto 
    if (int(mov_1 <0 )):
        return HttpResponse(f'Gasto agregado con exito ')
    elif (int(mov_1>0)):
        return HttpResponse(f'Ingreso agregado con exito ')
 
def dashboard(request):
    return HttpResponse("pagina de inicio")

def crear_usuario(request, Nombre, Apellido, Email, Contraseña):

    nuevo_usuario = usuario(Nombre= Nombre, Apellido= Apellido, Email= Email, Contraseña= Contraseña)
    nuevo_usuario.save()

    return HttpResponse('Usuario creado con éxito!')