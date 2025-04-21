from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto
from .forms import ProductoForm # Esto lo crearemos en el siguiente paso

# Vista para listar productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

# Vista para crear un producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'productos/crear_producto.html', {'form': form})

# Vista para editar un producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'productos/editar_producto.html', {'form': form})

# Vista para eliminar un producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')   
    
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})