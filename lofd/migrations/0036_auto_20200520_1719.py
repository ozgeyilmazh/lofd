# Generated by Django 2.2.4 on 2020-05-20 17:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0035_auto_20200520_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='movie',
            name='comment',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='series',
            name='comment',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Comment'),
        ),
    ]