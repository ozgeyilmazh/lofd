# Generated by Django 2.2.4 on 2020-05-09 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0009_auto_20200509_1828'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Desktops',
            new_name='Device',
        ),
        migrations.DeleteModel(
            name='Laptops',
        ),
        migrations.DeleteModel(
            name='Mobiles',
        ),
    ]
