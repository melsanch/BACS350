from django.shortcuts import render

class IndexView(TemplateView):
    model = Superhero
    template_name = 'index.html'

class HeroListView(ListView):
    model = Superhero
    template_name = 'hero_list.html'
