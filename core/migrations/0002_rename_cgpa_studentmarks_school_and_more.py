# Generated by Django 4.2.7 on 2024-01-09 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmarks',
            old_name='CGPA',
            new_name='school',
        ),
        migrations.RemoveField(
            model_name='studentmarks',
            name='result',
        ),
        migrations.RemoveField(
            model_name='studentmarks',
            name='totalmark',
        ),
    ]
