# Generated by Django 2.2.4 on 2020-05-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0002_auto_20200509_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
        migrations.AddField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='movies'),
        ),
        migrations.AddField(
            model_name='series',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='series'),
        ),
    ]
