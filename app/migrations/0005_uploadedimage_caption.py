# Generated by Django 4.2.6 on 2023-12-30 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='caption',
            field=models.TextField(default='Wow', max_length='20'),
        ),
    ]
