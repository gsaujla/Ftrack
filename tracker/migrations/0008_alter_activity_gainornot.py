# Generated by Django 5.0 on 2024-01-04 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_remove_activity_gain_activity_gainornot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='gainornot',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=100, null=True),
        ),
    ]
