# Generated by Django 5.0.7 on 2024-07-31 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Managment_System', '0002_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='status',
        ),
    ]
