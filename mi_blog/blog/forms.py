from django import forms
from .models import Publicacion
#Crear un formulario basado en el modelo "Publicacion"
class PublicacionModelForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categoria', 'autor']
    #Validación para "titulo" y "fecha_publicacion"
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo: 
            raise forms.ValidationError('El título no puede estar vacío.')
        return titulo
    def clean_fecha_publicacion(self):
        fecha_publicacion = self.cleaned_data.get('fecha_publicacion')
        if not fecha_publicacion:
            raise forms.ValidationError('La fecha de publicación es obligatoria.')
        return fecha_publicacion