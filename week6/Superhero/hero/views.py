from django.views.generic import RedirectView, CreateView, DetailView, ListView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Superhero
from django.shortcuts import render

class IndexView(TemplateView):
    model = Superhero
    template_name = 'index.html'

class HeroListView(ListView):
    model = Superhero
    template_name = 'hero_list.html'

class HeroDetailView(TemplateView):
    model = Superhero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Superhero.objects.get(pk=hero_id)

        
        return {'hero': hero
                
        }

class HeroView(RedirectView):
    url = '/hero/'

class HeroAddView(CreateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = ['name', 'identity', 'description', 'strength', 'weakness','image']

class HeroEditView(UpdateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = ['identity', 'description', 'strength', 'weakness']

class HeroDeleteView(DeleteView):
    template_name = "hero_delete.html"
    model = Superhero
    success_url = reverse_lazy('hero_list')