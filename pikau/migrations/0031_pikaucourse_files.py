# Generated by Django 2.0.5 on 2018-06-07 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
        ('pikau', '0030_auto_20180529_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='pikaucourse',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='pikau_courses', to='files.File'),
        ),
    ]