# Generated by Django 4.2.15 on 2024-09-14 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0007_alter_mailingsettings_stop_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='stop_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 15, 16, 38, 2, 935314), verbose_name='Конец рассылки'),
        ),
    ]
