from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

# Create your views here.

def home(request):
    usuarioListados = Usuario.objects.all()
    return render(request, "gestionQuejas.html", {"usuarios": usuarioListados})

def registrarQueja(request):
    if request.method == 'POST':
        codigo = request.POST.get('txtCodigo')
        nombre = request.POST.get('txtNombre')
        mensaje = request.POST.get('txtMensaje')
        piso = request.POST.get('numPiso')

        # Validar que todos los campos estén completos
        if not all([codigo, nombre, mensaje, piso]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('/')

        # Verificar si ya existe un usuario con ese código
        if Usuario.objects.filter(codigo=codigo).exists():
            messages.error(request, 'Error: ya existe una queja con ese código.')
            return redirect('/')

        Usuario.objects.create(codigo=codigo, nombre=nombre, mensaje=mensaje, piso=piso)
        messages.success(request, '¡Queja registrada con éxito!')
        return redirect('/')
    else:
        messages.error(request, 'Método no permitido.')
        return redirect('/')

def edicionQueja(request, codigo):
    queja = Usuario.objects.get(codigo=codigo)
    return render(request, "edicionQueja.html", {"queja":queja})

def editarQueja(request):
    codigo=request.POST ['txtCodigo']
    nombre=request.POST ['txtNombre']
    mensaje=request.POST ['txtMensaje']
    piso=request.POST ['numPiso']

    queja = Usuario.objects.get(codigo=codigo)
    queja.nombre = nombre
    queja.mensaje = mensaje
    queja.piso = piso
    queja.save()

    messages.success(request, 'Quejas Editado !')

    return redirect('/')



def eliminarQueja(request, codigo):
    queja = Usuario.objects.get(codigo=codigo)
    queja.delete()

    messages.success(request, 'Quejas Eliminadas !')

    return redirect('/')