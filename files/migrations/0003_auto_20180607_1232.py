# Generated by Django 2.0.5 on 2018-06-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_licence_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filename',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='location',
            field=models.URLField(unique=True),
        ),
    ]
