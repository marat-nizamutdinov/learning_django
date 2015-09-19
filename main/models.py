from django.db import models

# Create your models here.
class MainText(models.Model):
    head = models.CharField(verbose_name='Заголовок', max_length=200)
    text = models.CharField(verbose_name='Текст', max_length=900)
    image = models.ImageField(upload_to='main')

    def __str__(self):
        return self.head

    class Meta:
        verbose_name_plural = 'Текст главной страницы'
        verbose_name = 'текст'