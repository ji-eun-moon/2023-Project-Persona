# Generated by Django 3.2 on 2023-05-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='character',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.TextField(blank=True, null=True),
        ),
    ]
