# Generated by Django 4.1.5 on 2023-01-25 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_published_at_alter_postcomment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Introduction',
            field=models.CharField(default='دوست عزیز من بسیار خوشحالم که در حس نفیس وجود آرامش غرق شده ام.', max_length=76, verbose_name='introduction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 25, 5, 5, 46, 685517, tzinfo=datetime.timezone.utc), verbose_name='published at'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='email',
            field=models.EmailField(blank=True, max_length=120, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='fullname',
            field=models.CharField(blank=True, max_length=34, verbose_name='fullname'),
        ),
    ]
