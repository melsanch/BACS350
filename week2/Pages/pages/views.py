from django.shortcuts import render

from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'page.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'About this Class', 
            'body': 'Once upon a time ...',
        }
 
class HomeView(TemplateView):
    template_name = "home.html"
    
    

class IndexView(TemplateView):
    template_name = 'index.html'
 
 