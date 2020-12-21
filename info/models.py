from django.db import models


class InfoPage(models.Model):
    name = models.CharField('имя страницы', max_length=100, unique=True)
    text = models.TextField('содержание страницы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'страница с информацией'
        verbose_name_plural = 'страницы с информацией'


class Groups(models.Model):
    name = models.CharField('название группы', max_length=100, unique=True)
    image = models.ImageField('картинка группы', upload_to='media/groups')
