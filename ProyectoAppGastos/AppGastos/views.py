from django.http import HttpResponse
from django.shortcuts import render
from .models import movimientos, usuario
from django.http import response
# Create your views here.

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
            #return HttpResponse (f'Error, Por favor ingrese un numero en la seccion importe')
            return render (request,"ingreso_gasto-error.html", {'Fecha': Fecha ,'Categoria': Categoria,'Importe': Importe,'Nota':Nota,'Tipo_movimiento':Tipo_movimiento  })
    #Logica para diferenciar entre ingreso y gasto 
    if (int(mov_1 <0 )):
        return render (request,"ingresar_gasto.html", {'Fecha': Fecha ,'Categoria': Categoria,'Importe': Importe,'Nota':Nota,'Tipo_movimiento':Tipo_movimiento  })
    elif (int(mov_1>0)):
        return render (request,"ingresar_ingreso.html", {'Fecha': Fecha ,'Categoria': Categoria,'Importe': Importe,'Nota':Nota,'Tipo_movimiento':Tipo_movimiento  })

 
def inicio(request):
    return render (request,"Inicio.html")


def crear_usuario(request, Nombre, Apellido, Email, Contraseña):

    nuevo_usuario = usuario(Nombre= Nombre, Apellido= Apellido, Email= Email, Contraseña= Contraseña)
    nuevo_usuario.save()

    return render(request, 'usuario_creado.html')


def usuario_form(request):

    return render(request, "AppGastos/usuarioFormulario.html")


def movimientos_form(request):

    return render(request, "AppGastos/movimientosFormulario.html")