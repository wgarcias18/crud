from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def listar_producto(request):
    producto = Producto.objects.all()
    return render(request, 'listar_producto.html',{'producto':producto})

def crear_producto(request):
    producto = Producto(nombre=request.POST['nombre'], codigo=request.POST['codigo'], precio=request.POST['precio'], cantidad=request.POST['cantidad'], marca=request.POST['marca'])
    producto.save()
    return redirect('producto')

def eliminar_producto(request,producto_id):
    eliminar_producto = Producto.objects.get(id=producto_id)
    eliminar_producto.delete()
    return redirect('producto')


def editar_producto(resquest, producto_id):
    producto = Producto.objects.get(id=producto_id)
    forms = ProductoForm(resquest.POST or None, instance=producto)
    if forms.is_valid() and resquest.POST:
        forms.save()
        return redirect('producto')
    return render(resquest, 'editar_producto.html', {'forms': forms})