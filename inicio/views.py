from django.shortcuts import render, redirect
from django.http import HttpResponse 
from inicio.models import Auto
from inicio.forms import CrearAuto, BuscarAuto
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
   # return HttpResponse ('<h1>Hola soy el proyercto</h1>')
    return  render(request, 'inicio.html')

def otra(request):
  
    return  render(request, 'otra.html')
@login_required

def crear_auto(request):
    if request.method == 'POST':
        formulario = CrearAuto(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
        
            auto = Auto(marca=info.get('marca'), modelo=info.get('modelo'), imagen=info.get('imagen'))
            auto.save()
            
            return redirect('listado')
    else:
        formulario = CrearAuto()
    
    return render(request, 'crear_auto.html', {'formulario': formulario})

def listar_autos(request):
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        modelo_a_buscar = formulario.cleaned_data.get('modelo')
        listado_de_autos = Auto.objects.filter(modelo__icontains=modelo_a_buscar)
    return render(request, 'listar_autos.html', {'listado_de_autos': listado_de_autos, 'formulario': formulario})

def ver_auto(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    return render(request, 'ver_auto.html', {'auto': auto})

def index(request):
    return render(request, 'index.html')

def catalogo_autos(request):
    autos = Auto.objects.all()  
    return render(request, 'catalogo.html', {'autos': autos})

class ActualizarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = 'actualizar_auto.html'
    # fields = ['marca', 'modelo']
    fields = '__all__'
    success_url = reverse_lazy('listado')


class EliminarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = 'eliminar_auto.html'
    success_url = reverse_lazy('listado')

class AboutView(TemplateView):
    template_name = "about.html"