# Generated by Django 5.0 on 2024-01-04 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_alter_profile_balance_alter_profile_expenditure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='gain',
        ),
        migrations.AddField(
            model_name='activity',
            name='gainornot',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=100),
        ),
    ]
