# TallerPOO_BLOG
Blog básico utilizando Django, en el cual los usuarios podrán ver una lista de publicaciones, filtrar publicaciones por fecha o categoría, buscar publicaciones por título o contenido, y ver los detalles de una publicación específica.

# Características
Publicaciones: Listado de publicaciones con paginación, búsqueda, y filtrado.
Detalles de Publicación: Vista detallada de una publicación individual.
Agregar Publicaciones: Formulario para agregar nuevas publicaciones.
Navegación: Enlaces para navegar entre las publicaciones, regresar a la lista de publicaciones, y volver a la página de inicio.
# Estructura del Proyecto
blog/models.py: Contiene el modelo Publicacion.
blog/forms.py: Contiene el formulario PublicacionForm.
blog/views.py: Contiene las vistas de inicio, para listar publicaciones, ver detalles y agregar publicaciones.
blog/templates: Contiene las plantillas HTML para las diferentes vistas del blog.