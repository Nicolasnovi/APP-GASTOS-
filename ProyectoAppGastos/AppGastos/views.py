from django.http import HttpResponse
from django.shortcuts import render
from .models import movimientos, objetivo, usuario
from .forms import ObjetivoFormulario, MovimientosFormulario, UsuarioFormulario
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

    if request.method == "POST":

        miFormulario = UsuarioFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            nuevo_usuario = usuario(Nombre=informacion['Nombre'], Apellido=informacion['Apellido'], Email=informacion['Email'], Contraseña=informacion['Contraseña'])
            nuevo_usuario.save()
        
            return render(request, "usuario_creado.html")

    else:

        miFormulario = UsuarioFormulario()

    return render(request, "usuarioFormulario.html", {"miFormulario":miFormulario})


def movimientos_form(request):

    if request.method == "POST":

        miFormulario = MovimientosFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            nuevo_movimiento = movimientos(Fecha=informacion['Fecha'], Categoria=informacion['Categoria'], Importe=informacion['Importe'], Nota=informacion['Nota'], Tipo_movimiento=informacion['Tipo_movimiento'])
            nuevo_movimiento.save()
        
            return render(request, "ingresar_ingreso.html")

    else:

        miFormulario = MovimientosFormulario()

    return render(request, "movimientosFormulario.html", {"miFormulario":miFormulario})


def objetivo_form(request):

    if request.method == "POST":

        miFormulario = ObjetivoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            nuevo_objetivo = objetivo(Objetivo=informacion['Objetivo'], MontoDelObjetivo=informacion['MontoDelObjetivo'], Fecha=informacion['Fecha'], Observacion=informacion['Observacion'])
            nuevo_objetivo.save()
        
            return render(request, "objetivo_creado.html")

    else:

        miFormulario = ObjetivoFormulario()

    return render(request, "objetivoFormulario.html", {"miFormulario":miFormulario})


def busqueda_usuario(request):

    return render(request, "busqueda_usuario.html")


def buscar(request):

    if request.GET["Nombre"]:

        Nombre = request.GET['Nombre']
        usuarios = usuario.objects.filter(Nombre__icontains=Nombre)

        return render(request, "resultadosBusqueda.html", {"Nombre": Nombre, "contraseña": usuarios})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
