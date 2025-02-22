from django.views.generic import TemplateView


class MymapIndexView(TemplateView):
    template_name = 'mymap/index.html'
