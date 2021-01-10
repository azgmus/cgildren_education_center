from django.db import models


class KidsGroup(models.Model):

    name = models.CharField('название группы', max_length=30)
    image = models.ImageField('картинка группы', upload_to='media/KidsGroup')
    schedule = models.TextField('расписание')
