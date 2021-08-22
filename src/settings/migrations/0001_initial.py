# Generated by Django 3.2.4 on 2021-06-26 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRAName', models.CharField(max_length=120)),
                ('PRADesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VARName', models.CharField(max_length=120)),
                ('VARDesc', models.TextField()),
            ],
        ),
    ]