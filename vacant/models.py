from django.db import models

class Vacant(models.Model):
    vacancy = models.CharField(verbose_name='Вакансия',max_length=100)

    def __str__(self):
        return str(self.vacancy)

    class Meta:
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'