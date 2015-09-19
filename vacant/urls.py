from django.conf.urls import url
from vacant.views import VacantView

urlpatterns = [
    url(r'^$', VacantView.as_view(), name='vacant'),
]