# Generated by Django 3.1.6 on 2021-03-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210306_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_image',
            field=models.ImageField(default='', upload_to='home/img'),
        ),
    ]
