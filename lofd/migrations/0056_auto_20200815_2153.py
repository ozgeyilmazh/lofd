# Generated by Django 2.2 on 2020-08-15 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0055_auto_20200815_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookuserlist',
            name='booksComments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lofd.BookComment'),
        ),
        migrations.AlterField(
            model_name='bookcomment',
            name='booksList',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lofd.Book'),
        ),
    ]