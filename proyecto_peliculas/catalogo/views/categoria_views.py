from django.views.generic import TemplateView, DetailView, View
from catalogo.models import Categoria

class CategoriaTemplateView(TemplateView):
    model = Categoria
    template_name = "categorias.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = Categoria.objects.all().order_by("nombre")
        context["categorias"] = categorias
        return context

class CategoriaListView(DetailView):
    model = Categoria
    template_name = "peliculas_categoria.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = self.get_object()
        peliculas = categoria.peliculas.all()
        context["peliculas"] = peliculas
        return context

    
    


