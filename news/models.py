from django.db import models


class Article(models.Model):
    title = models.CharField('название статьи', max_length=40, unique=True)
    subtitle = models.CharField('подзаголовок статьи', max_length=340, blank=True)
    content = models.TextField('текст статьи')

    def __str__(self):
        return self.title
