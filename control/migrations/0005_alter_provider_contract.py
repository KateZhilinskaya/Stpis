# Generated by Django 3.2.16 on 2022-12-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_provider_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='contract',
            field=models.FileField(blank=True, null=True, upload_to='contacts'),
        ),
    ]
