# Generated by Django 4.0.5 on 2022-06-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20220310_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='reg_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]