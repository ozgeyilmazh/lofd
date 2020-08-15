# Generated by Django 2.2.4 on 2020-05-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lofd', '0015_auto_20200518_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title_de',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title_tr',
        ),
        migrations.RemoveField(
            model_name='trace',
            name='created_at',
        ),
    ]