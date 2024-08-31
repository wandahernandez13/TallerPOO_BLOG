from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion
from .forms import PublicacionModelForm
from django.db.models import Q
from django.core.paginator import Paginator

def inicio(request):
    return render(request, 'inicio.html')

def listar_publicaciones(request):
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
    return render(request, 'blog/lista_publicaciones.html', {'page_obj': page_obj})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})

def agregar_publicacion(request):
    if request.method == 'POST':
        form = PublicacionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_publicaciones')
    else:
        form = PublicacionModelForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('detalle_publicacion', pk=pk)
    else:
        form = PostForm(instance=publicacion)
    return render(request, 'editar_publicacion.html', {'form': form})