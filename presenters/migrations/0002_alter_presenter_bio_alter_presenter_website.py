# Generated by Django 5.1 on 2024-09-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presenters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenter',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presenter',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
