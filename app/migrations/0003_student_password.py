# Generated by Django 4.2.6 on 2023-12-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
