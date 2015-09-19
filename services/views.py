from main.views import MainView
from .models import ServiceType


class IndexView(MainView):
    model = ServiceType
    template_name = 'index.html'
    context_object_name = 'service_list'