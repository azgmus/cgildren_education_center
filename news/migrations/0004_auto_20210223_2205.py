# Generated by Django 3.1.4 on 2021-02-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='название статьи'),
        ),
    ]