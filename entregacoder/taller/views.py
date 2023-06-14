from django.shortcuts import render
from django.http import HttpResponse
from .models import Herramienta, Operario, Lider, Consumible
from .forms import FormularioHerramienta, BuscaOperario, FormularioLider, FormularioOperario, FormularioConsumible

def inicio(request):
    return render(request, "taller/index.html")

def lideres(request):
    return render(request, "taller/lideres.html")

def operarios(request):
    return render(request, "taller/operarios.html")

def herramientas(request):
    return render(request, "taller/herramientas.html")

def consumibles(request):
    return render(request, "taller/consumibles.html")

def leerHerramientas(request):
    
    herramientas = Herramienta.objects.all()
    contexto = {"Herramientas": herramientas}
    return render(request, "taller/herramientas.html", contexto)

def leerOperarios(request):
    
    operarios = Operario.objects.all()
    contexto = {"Operarios": operarios}
    return render(request, "taller/operarios.html", contexto)

def leerLideres(request):
    
    lideres = Lider.objects.all()
    contexto = {"Lideres": lideres}
    return render(request, "taller/lideres.html", contexto)

def leerConsumibles(request):
    
    consumibles = Consumible.objects.all()
    contexto = {"Consumibles": consumibles}
    return render(request, "taller/consumibles.html", contexto)

def herramientasFormulario(request):
    
    if request.method =='POST':
        miFormulario = FormularioHerramienta(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            herramienta = Herramienta(nombre=informacion['nombre'], rastreo=informacion['rastreo'], calibracion=informacion['calibracion'], operario=informacion['operario'], descripcion=informacion['descripcion'])
            herramienta.save()
            return render(request, "taller/index.html")
    else:
        miFormulario = FormularioHerramienta()
    return render(request, "taller/herramientaFormulario.html",{"miFormulario": miFormulario})


def liderFormulario(request):
    
    if request.method =='POST':
        miFormulario = FormularioLider(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            lider = Lider(nombre=informacion['nombre'], apellido=informacion['apellido'], legajo=informacion['legajo'], sector=informacion['sector'])
            lider.save()
            return render(request, "taller/index.html")
    else:
        miFormulario = FormularioLider()
    return render(request, "taller/liderFormulario.html",{"miFormulario": miFormulario})


def operarioFormulario(request):
    
    if request.method =='POST':
        miFormulario = FormularioOperario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            operario = Operario(nombre=informacion['nombre'], apellido=informacion['apellido'], legajo=informacion['legajo'], lider=informacion['lider'], descripcion=informacion['descripcion'])
            operario.save()
            return render(request, "taller/index.html")
    else:
        miFormulario = FormularioOperario()
    return render(request, "taller/OperarioFormulario.html",{"miFormulario": miFormulario})


def consumibleForm(request):
    
    if request.method =='POST':
        miFormulario = FormularioConsumible(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            consumible = Consumible(nombre=informacion['nombre'], descripcion=informacion['descripcion'], cantidad=informacion['cantidad'], unidad=informacion['unidad'])
            consumible.save()
            return render(request, "taller/index.html")
    else:
        miFormulario = FormularioConsumible()
    return render(request, "taller/consumiblesFormulario.html",{"miFormulario": miFormulario})


def buscar(request):
    if request.method=="POST":
        busca_operario = BuscaOperario(request.POST)
        
        if busca_operario.is_valid():
            info = busca_operario.cleaned_data
            operarios = Operario.objects.filter(apellido__icontains=info["apellido"])
            return render(request, "taller/resultadoBusqueda.html", {"operarios": operarios})
    else:
        busca_operario= BuscaOperario()
        return render(request, "taller/BuscaOperario.html", {"miFormulario":busca_operario})