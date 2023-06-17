from django.views import generic
from ..models.language import Language

class LanguageListView(generic.ListView):
    model = Language
    queryset = Language.objects.all()
    template_name = 'language_list.html'

class LanguageDetailView(generic.DetailView):
    model = Language
    template_name = 'language_detail.html'