from django.shortcuts import render
from django.http import HttpResponse
from Entregable.forms import DestinosForm, DatosForm
from Entregable.models import Datos, Destinos

# Create your views here.
def destinos(request):
    lista = Destinos.objects.all()
    return render(request, 'Entregable/destinos.html', {"lista": lista})

def destinoForm(request):
    #print(request.POST) ### Nota: Validar lo que viene en el POST. ###
    if(request.method == 'POST'):
        miForm = DestinosForm(request.POST)
        if(miForm.is_valid()):
            destino = Destinos(pais=request.POST["pais"], ciudad=request.POST["ciudad"])
            destino.save()
            return render(request, "Entregable/inicio.html")
    else:
        miForm = DestinosForm()
    return render(request, "Entregable/destinoForm.html", {'miForm': miForm})


def personas(request):
    lista = Datos.objects.all()
    return render(request, 'Entregable/personas.html', {"lista": lista})

def datosForm(request):
    if(request.method == 'POST'):
        miForm = DatosForm(request.POST)
        if(miForm.is_valid()):
            datos = Datos(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
            datos.save()
            return render(request, "Entregable/inicio.html")
    else:
        miForm = DatosForm()
    return render(request, "Entregable/datosForm.html", {'miForm': miForm})


def busquedaDestino(request):

    return render(request, 'Entregable/busquedaDestino.html')

def buscarDestino(request):

    if(request.method == 'GET'):

        pais = request.GET["pais"]
        ciudades = Destinos.objects.filter(pais=pais)

        return render(request, "Entregable/resultadosBusqueda.html", {'ciudades': ciudades, 'pais': pais})
    
    else:

        return HttpResponse('No enviaste datos')

def inicio (request):

    return render(request, 'Entregable/inicio.html')