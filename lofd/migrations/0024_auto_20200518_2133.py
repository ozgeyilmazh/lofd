# Generated by Django 2.2.4 on 2020-05-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0023_auto_20200518_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='lofd.Author'),
        ),
    ]
