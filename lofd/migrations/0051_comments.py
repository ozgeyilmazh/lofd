# Generated by Django 2.2.4 on 2020-05-24 22:18

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lofd', '0050_watchuserlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', ckeditor.fields.RichTextField(max_length=350)),
                ('booksList', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lofd.Book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watchesList', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lofd.Watch')),
            ],
        ),
    ]
