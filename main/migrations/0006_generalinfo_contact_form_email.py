# Generated by Django 3.1.4 on 2021-05-31 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210308_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='contact_form_email',
            field=models.CharField(max_length=50, null=True, verbose_name='имейл, на который будет приходить сообщение с контактной формы'),
        ),
    ]
