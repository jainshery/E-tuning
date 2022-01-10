# Generated by Django 3.1.4 on 2021-04-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_artist2_retypepass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist2',
            name='city',
        ),
        migrations.RemoveField(
            model_name='artist2',
            name='state',
        ),
        migrations.RemoveField(
            model_name='register',
            name='city',
        ),
        migrations.RemoveField(
            model_name='register',
            name='state',
        ),
        migrations.AddField(
            model_name='artist2',
            name='username',
            field=models.CharField(default='none', max_length=150, verbose_name='User Name'),
        ),
        migrations.AddField(
            model_name='register',
            name='des',
            field=models.TextField(default='empty'),
        ),
        migrations.AddField(
            model_name='register',
            name='image',
            field=models.ImageField(default='', upload_to='C:\\proper_project\\djangoproj\\etuning\\static\\img'),
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default='none', max_length=150, verbose_name='User Name'),
        ),
    ]