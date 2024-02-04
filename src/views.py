from django.views.generic import TemplateView, ListView
from src.models import PhrasalVerbs

# Create your views here.

class PhrasalVerbsView(ListView):
    model = PhrasalVerbs
    template_name = 'phrasal_verbs.html'
    context_object_name = 'verbs'

    group_by = {start.phrasal_verb.split(' ')[0] for start in PhrasalVerbs.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {}

        for start in self.group_by:
            queryset = PhrasalVerbs.objects.filter(phrasal_verb__istartswith=start)
            data[start] = queryset

        context['verbs_dict'] = data
        context['text'] = 'fsdfs \n fasdf'

        return context

class HomeView(TemplateView):
    template_name = 'Home.html'
