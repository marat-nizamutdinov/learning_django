import os
from django.db import models
from PIL import Image, ImageOps

class Slider(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='slider')
    comment = models.CharField(verbose_name='Комментарий',max_length=100, blank=True)

    def __str__(self):
        return self.image.url

    def delete(self, *args, **kwargs):
        super(Slider, self).delete(*args, **kwargs)
        os.remove(self.image.path)

    def save(self, *args, **kwargs):
        try:
            slide = Slider.objects.get(id=self.id)
            if slide.image != self.image:
                slide.image.delete()
        except: pass

        super(Slider, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        img = ImageOps.fit(img, (1200, 300), Image.ANTIALIAS)
        img.save(self.image.path, quality=100)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Слайдер изображений'