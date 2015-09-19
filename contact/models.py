from django.db import models


class Contact(models.Model):
    person_name = models.CharField(verbose_name='Имя', max_length=100)
    person_last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    person_phone = models.CharField(verbose_name='Телефон', max_length=20)
    person_mail = models.EmailField(verbose_name='E-mail', max_length=40)

    def __str__(self):
        return self.person_name + " " + self.person_last_name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = 'Контакты'