# Generated by Django 3.2.16 on 2022-12-16 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221215_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='accounts.company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.IntegerField(choices=[(0, 'Сотрудник'), (2, 'Владелец'), (1, 'Отдел закупок')], verbose_name='Должность'),
        ),
    ]
