# Generated by Django 3.2.16 on 2022-12-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0012_auto_20221217_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='fio',
        ),
        migrations.AddField(
            model_name='orderpart',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='orderpart',
            name='fio',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО получателя'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.IntegerField(choices=[(4, 'Отклонена'), (0, 'Cоздана'), (2, 'Принята'), (3, 'Завершена'), (1, 'Отправлена')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Сформирован'), (0, 'Создан')], default=0, verbose_name='Статус'),
        ),
    ]
