from django.db import models


class Picture(models.Model):
    image = models.ImageField(upload_to='media/gallery')
    description = models.CharField('описание', max_length=40)


    class Meta:
        verbose_name = 'картинки галлереи'
        verbose_name_plural = 'картинки галлереи'

    def __str__(self):
        return self.description