# Generated by Django 3.2 on 2022-03-09 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20220309_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
