# Generated by Django 4.2.6 on 2023-12-23 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Phone',
            field=models.BigIntegerField(),
        ),
    ]
