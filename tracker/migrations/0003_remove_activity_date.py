# Generated by Django 5.0 on 2024-01-04 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_profile_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='date',
        ),
    ]
