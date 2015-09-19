from django import forms
import re
from django.core.mail import send_mail
from learning_django.settings import FEEDBACK_RECIPIENTS


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_subject(self):
        not_valid_char = re.compile('^[а-яА-ЯёЁa-zA-Z0-9]+$')
        data = self.cleaned_data['subject']
        match = not_valid_char.search(data)

        if len(data) < 2:
            raise forms.ValidationError('В вашем имени не может быть меньше 2 символов')

        if not match:
            raise forms.ValidationError('Вы использовали недопустимые символы')

        return data

    def send_mail(self):

        send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['sender'] + ' прислал вам сообщение на чистик-спб: ' + self.cleaned_data['message'],
            self.cleaned_data['sender'],
            FEEDBACK_RECIPIENTS
        )
