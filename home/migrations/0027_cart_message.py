# Generated by Django 3.2 on 2021-05-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20210428_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='message',
            field=models.BooleanField(default=True),
        ),
    ]
