from django.shortcuts import render, redirect
from .models import Pais
from .models import Prooveedor


# Create your views here.
def listar_Pais(request):
    pais = Pais.objects.all()
    return render(request, 'listar_Pais.html',{'pais':pais})

def crear_pais(request):
    pais = Pais(nombre=request.POST['nombre'], estado=request.POST['estado'])
    pais.save()
    return redirect('pais')

def listar_Proveedor(request):
    proveedor = Prooveedor.objects.all()   #filter(status=True)
    return render(request, 'listar_proveedor.html',{'proveedor':proveedor})


def crear_Proveedor(request):
    proveedor = Prooveedor(pais=request.POST['pais'], nombre=request.POST['nombre'], estado=request.POST['estado'], marca=request.POST['marca'])
    proveedor.save()
    return redirect('proveedor')


