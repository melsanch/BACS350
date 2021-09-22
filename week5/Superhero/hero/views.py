from django.views.generic import ListView, TemplateView
from .models import Superhero

class IndexView(TemplateView):
    model = Superhero
    template_name = 'index.html'
