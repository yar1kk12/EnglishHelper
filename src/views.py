from django.views.generic import TemplateView, ListView
from src.models import PhrasalVerbs
from django.db.models import Q

# Create your views here.

class PhrasalVerbsView(ListView):
    model = PhrasalVerbs
    template_name = 'phrasal_verbs.html'
    context_object_name = 'verbs'

    group_by = {start.phrasal_verb.split(' ')[0] for start in PhrasalVerbs.objects.all()}


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search = self.request.GET.get(' search', '')
    #
    #     if search:
    #         queryset = queryset.filter(
    #             Q(phrasal_verb__icontains=search)
    #         )
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search', '')
        data = {}

        if search:
            queryset = PhrasalVerbs.objects.all()
            queryset = queryset.filter(
                Q(phrasal_verb__icontains=search)
            )
            context['search'] = queryset
        else:
            for start in sorted(self.group_by):
                queryset = PhrasalVerbs.objects.filter(phrasal_verb__istartswith=start)
                data[start] = queryset

            context['verbs_dict'] = data

        return context

class HomeView(TemplateView):
    template_name = 'Home.html'
