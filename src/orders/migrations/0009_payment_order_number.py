# Generated by Django 3.2.4 on 2021-08-31 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210830_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]