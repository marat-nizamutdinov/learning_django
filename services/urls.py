from django.conf.urls import url
from services.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='services'),
]