from django.db import models


class KidsGroup(models.Model):

    name = models.CharField('название группы', max_length=30)
    image = models.ImageField('картинка группы', upload_to='media/KidsGroup')
    schedule = models.TextField('расписание')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "группа детей"
        verbose_name_plural = "группы детей"
