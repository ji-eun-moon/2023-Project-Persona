# Generated by Django 3.2 on 2023-05-21 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_review_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
