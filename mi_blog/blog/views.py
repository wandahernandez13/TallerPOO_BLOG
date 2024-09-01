from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion
from .forms import PublicacionForm
from django.db.models import Q
from django.core.paginator import Paginator


def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    # Filtrado:
    fecha_publicacion = request.GET.get('fecha_publicacion')
    categoria = request.GET.get('categoria')
    if fecha_publicacion:
        publicaciones = publicaciones.filter(fecha_publicacion=fecha_publicacion)
    if categoria:
        publicaciones = publicaciones.filter(categoria__icontains=categoria)

    # Búsqueda:
    query = request.GET.get('q')
    if query:
        publicaciones = publicaciones.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        )
    
    # Paginación:
    paginator = Paginator(publicaciones, 10)  # 10 publicaciones por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/lista_publicaciones.html', {
        'page_obj': page_obj, 
        'query': query,
        'categoria': categoria,
        'fecha_publicacion': fecha_publicacion,
        })

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)

    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})

def agregar_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()

    return render(request, 'blog/agregar_publicacion.html', {'form': form})

def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm(instance=publicacion)

    return render(request, 'blog/editar_publicacion.html', {'form': form, 'publicacion': publicacion})