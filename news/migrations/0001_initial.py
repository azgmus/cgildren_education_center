# Generated by Django 3.1.4 on 2021-02-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='название страницы')),
                ('content', models.TextField(verbose_name='текст страницы')),
            ],
        ),
    ]
