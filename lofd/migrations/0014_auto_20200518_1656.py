# Generated by Django 2.2.4 on 2020-05-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0013_auto_20200518_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title_de',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title_fr',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title_tr',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trace',
            name='title_de',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trace',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trace',
            name='title_fr',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trace',
            name='title_tr',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
