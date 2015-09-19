from django.db import models

class ServiceType(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

class Service(models.Model):
    type = models.ForeignKey(ServiceType)
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name
