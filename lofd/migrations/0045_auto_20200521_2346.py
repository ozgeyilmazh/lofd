# Generated by Django 2.2.4 on 2020-05-21 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0044_auto_20200521_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookuserlist',
            name='booksList',
            field=models.ManyToManyField(to='lofd.Book'),
        ),
    ]
