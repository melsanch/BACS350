from django.views.generic import RedirectView, TemplateView
from markdown import markdown

class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = 'Hero'
        markdown_text = open(f'Documents/{document}.md').read()
        return dict(doc=markdown(markdown_text), file=document)
