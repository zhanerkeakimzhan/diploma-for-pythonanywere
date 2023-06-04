# Generated by Django 4.2 on 2023-05-25 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard2', '0014_userprofile_chairman_alter_userprofile_commission'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='chairman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bboard2.chairmans'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='commission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bboard2.commissions'),
        ),
    ]