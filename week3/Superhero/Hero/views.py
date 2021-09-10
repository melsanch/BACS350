from django.views.generic import TemplateView


class HulkView(TemplateView):
    template_name = 'hulk.html'
    
    
 
class IronManView(TemplateView):
    template_name = "iron_man.html"
    
    

class BlackWidowView(TemplateView):
    template_name = 'black_widow.html'

class IndexView(TemplateView):
    template_name = 'index.html'