# Generated by Django 4.1.5 on 2023-01-20 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 19, 23, 52, 255805, tzinfo=datetime.timezone.utc), verbose_name='published at'),
        ),
    ]
