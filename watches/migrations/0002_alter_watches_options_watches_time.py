# Generated by Django 5.1.2 on 2024-11-16 09:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watches',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Watches'},
        ),
        migrations.AddField(
            model_name='watches',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
