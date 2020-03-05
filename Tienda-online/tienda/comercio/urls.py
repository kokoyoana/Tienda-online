from django.urls import path
from .views import *



urlpatterns = [
    path('',Consultar.as_view(), name = 'inicio'),
    path('ella/',ConsultarElla.as_view(), name = 'ella'),
    path('el/',ConsultarEl.as_view(), name = 'el'),
    path('agregar/<int:pk>',AgregarCarrito.as_view(), name = 'agregar'),
    path('eliminar/<int:pk>/',EliminarProd.as_view(), name = 'eliminar'),
    path('vercar/',ConsultarCarrito.as_view(), name = 'vercar'),
    path('pagar/',Pagar.as_view(), name = 'pagar'),
    

    
]