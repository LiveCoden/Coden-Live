# Generated by Django 3.2.4 on 2021-12-24 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogModel',
            new_name='Blog',
        ),
    ]
