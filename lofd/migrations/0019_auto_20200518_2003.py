# Generated by Django 2.2.4 on 2020-05-18 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0018_auto_20200518_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lofd.Author'),
        ),
    ]
