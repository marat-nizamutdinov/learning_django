from django.views.generic import ListView

from main.models import MainText
from slider.models import Slider


class MainView(ListView):
    model = MainText
    template_name = 'main.html'
    context_object_name = 'main_text'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.all()
        return context