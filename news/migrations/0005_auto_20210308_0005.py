# Generated by Django 3.1.4 on 2021-03-07 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210223_2205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
    ]