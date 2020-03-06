from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, View
from .models import Producto, Carrito
from django.urls import reverse_lazy
from .forms import CarritoForm

#nos lleva a inicio
class Consultar(ListView):
    model = Producto
    template_name = 'comercio/index.html'
    context_object_name = 'pro'
    queryset = Producto.objects.all()

#nos lleva a ella
class ConsultarElla(ListView):
    model = Producto
    template_name = 'comercio/paraElla.html'
    context_object_name = 'pro'
    queryset = Producto.objects.filter(tipo='F')

#nos lleva a el
class ConsultarEl(ListView):
    model = Producto
    template_name = 'comercio/paraEl.html'
    context_object_name = 'pro'
    queryset = Producto.objects.filter(tipo='M')

#nos lleva a el
class ConsultarParejas(ListView):
    model = Producto
    template_name = 'comercio/parejas.html'
    context_object_name = 'pro'
    queryset = Producto.objects.filter(tipo='P')




#VA EN EL BOTON DE CARRITO
class AgregarCarrito(CreateView):
    model = Carrito
    form_class = CarritoForm
    template_name = 'comercio/agregar.html'
    success_url = reverse_lazy('comercio:vercar')

    def form_valid(self, form):
        self.object = form.save(commit=False) 
        var= Producto.objects.get(pk=self.kwargs.get('pk', None))
        self.object.idPro=var
        subTotal = self.object.cantidad*var.precio
        self.object.subTotal = subTotal
        self.object.save()
        return super(AgregarCarrito, self).form_valid(form)



#ELIMINA CADA UNIDAD DE PRODUCTO 
class EliminarProd(DeleteView):
    model = Carrito
    success_url = reverse_lazy('comercio:vercar')  

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, kwargs)

#VEMOS TODOS LOS PRODUCTOS DEL CARRITO
class ConsultarCarrito(ListView):
    model = Carrito
    template_name = 'comercio/carrito.html'
    context_object_name = 'pro'
    queryset = Carrito.objects.all()




#VACIAR EL CARRITO DE COMPRA
class Pagar(View):
    model = Carrito
    def get(self, request, *args, **kwargs):
        Carrito.objects.all().delete()
        return redirect('comercio:vercar')

        
class VerFormulario(ListView):
    model = Producto
    template_name = 'comercio/formulario.html'
    