from django.db import models


class Article(models.Model):
    title = models.CharField('название страницы', max_length=40, unique=True)
    content = models.TextField('текст страницы')

    def __str__(self):
        return self.title
