from django import forms
from .models import Producto, Carrito



class CarritoForm(forms.ModelForm):
	class Meta:				
	    model = Carrito
	    fields = ['cantidad']
	    labels = {'cantidad': 'Cantidad del producto',
				}

	    widgets = {
                    'cantidad': forms.TextInput(attrs = {'class': 'form-control', 'id':'cantidad'}),
	    }