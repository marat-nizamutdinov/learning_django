from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.views.generic import FormView

from .forms import ContactForm
from slider.models import Slider


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_mail()
        return super(ContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        response = super(ContactView, self).get(request, *args, **kwargs)
        response.set_cookie('has_thanksgived', False )
        return response


def thanks(request):
    if request.session.get('has_thanksgived'):
        request.session['has_thanksgived'] = True
        return render(request, 'thanks.html', {
            'slider': Slider.objects.all(),
            'additional_scripts': [static('js/contact.js')]
        })
    else:
        return redirect(reverse('main'))