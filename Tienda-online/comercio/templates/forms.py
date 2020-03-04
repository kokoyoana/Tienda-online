from django import forms
from .models import Producto



class ProForm(forms.ModelForm):
	class Meta:				
	    model = Producto
	    fields = ['nombre', 'descripcion', 'precio']
	    labels = {'nombre': 'Nombre del producto',
				'descripcion':'Descripcion del Producto',
				'precio': 'Precio del producto'}

	    widgets = {
                    'nombre': forms.TextInput(attrs = {'class': 'form-control', 'id':'nombre'}),
	    		    'descripcion': forms.TextInput(attrs = {'class': 'form-control', 'id':'descripcion'}),
	    			'precio': forms.NumberInput(attrs = {'class': 'form-control', 'id':'precio'}),
	    }