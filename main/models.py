from django.db import models


class KidsGroup(models.Model):

    name = models.CharField('название группы', max_length=30)
    image = models.ImageField('картинка группы', upload_to='media/KidsGroup')
    schedule = models.TextField('расписание')
    da = models.AutoField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "группа детей"
        verbose_name_plural = "группы детей"


class InfoPages(models.Model):
    name = models.CharField('название страницы', max_length=40, unique=True)
    content = models.TextField('текст страницы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "дополнительная страница"
        verbose_name_plural = "дополнительные страницы"


class GeneralInfo(models.Model):
    contact_email = models.CharField('имейл, который будет показываться на каждой странице сайта', max_length=50)
    contact_phone = models.CharField('номер телефона, который будет показываться на каждой странице сайта', max_length=50)

    class Meta:
        verbose_name = "общая информация"
        verbose_name_plural = "общая информация"
