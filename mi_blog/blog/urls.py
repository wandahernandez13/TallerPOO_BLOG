from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='inicio'),  # Ruta raíz que apunta a la vista lista_publicaciones
    path('publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('agregar_publicacion/', views.agregar_publicacion, name='agregar_publicacion'),
    path('editar/<int:pk>/', views.editar_publicacion, name='editar_publicacion'),
]