# Generated by Django 4.2 on 2023-05-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard2', '0007_defense_coment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defense',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='defense',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
