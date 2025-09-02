from django.shortcuts import render
from .models import Historia, Categoria

def home(request):
    historias = Historia.objects.all().order_by('-fecha_creacion')
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {
        'historias': historias,
        'categorias': categorias
    })
