# Generated by Django 3.2.4 on 2021-06-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
