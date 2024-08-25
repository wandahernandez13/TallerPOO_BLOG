from django import forms
from .models import Publicacion
#Crear un formulario basado en el modelo "Publicacion"
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categoria', 'autor']
    #Validación para "titulo"
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo: 
            raise forms.ValidationError('El título no puede estar vacío.')
        return titulo