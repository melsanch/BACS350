from django.views.generic import ListView, TemplateView
from .models import Hero

class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'

class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'

class IndexView(TemplateView):
    template_name = 'index.html'