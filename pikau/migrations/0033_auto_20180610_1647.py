# Generated by Django 2.0.6 on 2018-06-10 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pikau', '0032_auto_20180609_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pikaucourse',
            name='project_item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pikau_course', to='files.ProjectItem'),
        ),
    ]
