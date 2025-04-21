from django import forms
from .models import Producto  # Asegúrate de que `Producto` está en `models.py`

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']