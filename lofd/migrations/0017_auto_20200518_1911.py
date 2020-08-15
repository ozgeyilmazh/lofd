# Generated by Django 2.2.4 on 2020-05-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0016_auto_20200518_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('lastName', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Writer',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='lofd.Author'),
        ),
    ]