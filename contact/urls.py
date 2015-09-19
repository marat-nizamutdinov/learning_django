from django.conf.urls import url
from contact.views import ContactView

urlpatterns = [
    url(r'^$', ContactView.as_view(success_url='contact/thanks/'), name='contact'),
    url(r'thanks/$', 'contact.views.thanks', name='thx'),
]