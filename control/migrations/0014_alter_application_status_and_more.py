# Generated by Django 4.1.4 on 2022-12-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0013_auto_20221217_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.IntegerField(choices=[(2, 'Принята'), (0, 'Cоздана'), (3, 'Завершена'), (1, 'Отправлена'), (4, 'Отклонена')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='externalcontract',
            name='contract',
            field=models.FileField(upload_to='contracts/external', verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='internalcontract',
            name='contract',
            field=models.FileField(upload_to='contracts/internal', verbose_name='Договор'),
        ),
    ]
