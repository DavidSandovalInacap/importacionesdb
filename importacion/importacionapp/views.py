# estoy importando los modulos y clases necesarias
from django.shortcuts import render, redirect

from .models import Importacion, Boleta
from .forms import ImportacionForm
# Create your views here.

# se definen las vistas que manejan las solicitudes del usuario
def inicio(request):
     # esta es la vista para la página de inicio.
    return render(request, 'paginas/inicio.html')

def lista_importacion(request):
    # esta es la vista para la lista de importaciones.
    return render(request, 'paginas/lista_importacion.html')

def importaciones(request):
    #esta es la vista para mostrar todas las importaciones.
    importaciones = Importacion.objects.all()
    return render(request, 'importaciones/index.html', {'importaciones': importaciones})

def crear(request):
    # esta es la vista para crear una nueva importación utilizando el formulario ImportacionForm.
    formulario = ImportacionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('importaciones')
    return render(request, 'importaciones/crear_importacion.html', {'formulario': formulario})

def boleta(request, id):
     # esta es la vista para mostrar los detalles de una boleta de importación.
    importacion = Importacion.objects.get(id=id)
    boleta = Boleta.objects.get(id_importacion=importacion)

    return render(request, 'importaciones/boleta_importacion.html', {'boleta': boleta})


def boleta(request, id):
    importacion = Importacion.objects.get(id=id)

    # Calcula el costo de envío en pesos chilenos
    costo_envio_usd = importacion.costo_envio
    costo_envio_clp = costo_envio_usd * 890

    # Corrige el cálculo del total del pedido en CLP
    total_importacion_clp = int(importacion.unidades) * importacion.costo_unitario * 890

    cif = costo_envio_clp + total_importacion_clp
    tasa_aduana = cif * 0.06
    iva = cif * 0.19
    impuestos = tasa_aduana + iva

    # Corrige el cálculo de valor_dolares
    valor_dolares = (total_importacion_clp + costo_envio_clp + impuestos) / 890

    # Crea la instancia de Boleta con el costo de envío en CLP y el total del pedido corregido
    boleta = Boleta.objects.create(
        id_importacion=importacion,
        total_importacion=total_importacion_clp,  # Corrección en el total del pedido
        costo_envio=costo_envio_clp,
        cif=cif,
        tasa_aduana=tasa_aduana,
        iva=iva,
        impuestos=impuestos,
        total_compra=cif + impuestos,  # Corrección en el cálculo del costo total de la compra en CLP
        valor_dolares=valor_dolares  # Corrección en el cálculo de valor_dolares
    )

    # Pasa la boleta como contexto a la plantilla
    return render(request, 'importaciones/boleta_importacion.html', {'boleta': boleta})



    

