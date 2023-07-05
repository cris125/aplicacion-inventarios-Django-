from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from . models import Productos
from django.contrib import messages

# Create your views here.
def index(request):
  product = Productos.objects.all().values()
  template = loader.get_template('add.html')
  context = {
    'product': product,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  product = Productos.objects.all().values()
  template = loader.get_template('add.html')
  context = {
    'product': product,
  }
  return HttpResponse(template.render(context, request))
def agre(request):  
  name = request.POST['nameT']
  price = request.POST['priceT']
  existence=request.POST['existenceT']
  
  producto = Productos.objects.create(
    name=name,price=price,existence=existence
  )
  messages.success(request, '¡Curso registrado!')
  return redirect("/")

def eliminar(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/')

def edicionP(request, id):
    producto = Productos.objects.get(id=id)
    return render(request, "edicionP.html", {"producto": producto})


def editarP(request,id):
    name = request.POST['nameT']
    price = request.POST['priceT']
    existence=request.POST['existenceT']

    producto = Productos.objects.get(id=id)
    producto.name = name
    producto.price = price
    producto.existence=existence
    producto.save()
    messages.success(request, '¡Curso actualizado!')

    return redirect('/')
"""
  name = request.POST['name']
  price = request.POST['price']
  existence=request.POST['existence']
  
  product = Productos.objects.create(
    name=name,price=price,existence=existence
  )
  return redirect("inventarios")"""
  

