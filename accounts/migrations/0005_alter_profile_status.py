# Generated by Django 3.2.16 on 2022-12-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.IntegerField(choices=[(0, 'Сотрудник'), (2, 'Владелец'), (1, 'Отдел закупок')], verbose_name='Должность'),
        ),
    ]
