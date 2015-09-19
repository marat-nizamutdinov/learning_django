from contact.models import Contact
from main.views import MainView
from .models import Vacant


class VacantView(MainView):
    model = Vacant
    template_name =  'vacant.html'
    context_object_name = 'vacant_list'

    def get_context_data(self, **kwargs):
        context = super(VacantView, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.all()
        return context