from django.urls import path
from .views import inicio, listar_publicaciones, detalle_publicacion, agregar_publicacion, editar_publicacion

urlpatterns = [
    path('publicaciones', listar_publicaciones, name='lista_publicaciones'),
    path('publicacion/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
    path('agregar_publicacion/', agregar_publicacion, name='agregar_publicacion'),
    path('inicio/', inicio, name='inicio'),
    path('editar/<int:pk>/', editar_publicacion, name='editar_publicacion'),
]