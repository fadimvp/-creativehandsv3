# Generated by Django 3.2.4 on 2021-09-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210911_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lang',
            field=models.CharField(blank=True, choices=[('1', 'ar'), ('en', 'en')], max_length=255),
        ),
        migrations.AlterField(
            model_name='settinglang',
            name='lang',
            field=models.CharField(blank=True, choices=[('1', 'ar'), ('en', 'en')], max_length=6),
        ),
    ]
