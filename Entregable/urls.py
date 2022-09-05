from django.urls import path
from Entregable import views


urlpatterns = [
    path('', views.inicio, name="Inicio"), # Primera View
    path('destinos/', views.destinos, name="Destinos"),
    path('destinoForm/', views.destinoForm, name="DestinoFormulario"),
    path('personas/', views.personas, name ="Personas"),
    path('datosForm/', views.datosForm, name ="DatosFormulario"),
    path('busquedaDestino/', views.busquedaDestino, name="BusquedaDestino"),
    path('buscarDestino/', views.buscarDestino, name="BuscarDestino"),
]