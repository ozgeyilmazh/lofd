# Generated by Django 2.2 on 2020-08-15 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0054_auto_20200528_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcomment',
            name='booksList',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lofd.Book'),
        ),
    ]
