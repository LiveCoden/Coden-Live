# Generated by Django 3.2.4 on 2021-06-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demoform',
            name='phone',
            field=models.TextField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
