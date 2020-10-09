# Generated by Django 2.2.4 on 2020-05-22 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0045_auto_20200521_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookuserlist',
            name='booksList',
        ),
        migrations.AddField(
            model_name='bookuserlist',
            name='booksList',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lofd.Book'),
            preserve_default=False,
        ),
    ]
