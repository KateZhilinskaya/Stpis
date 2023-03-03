# Generated by Django 3.2.16 on 2022-12-16 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_status'),
        ('control', '0006_externalcontract_internalcontract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('status', models.IntegerField(choices=[(2, 'Завершена'), (0, 'Отправлена'), (3, 'Отклонена'), (1, 'Принята')], default=0, verbose_name='Статус')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='accounts.company', verbose_name='Компании')),
                ('contract', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.internalcontract', verbose_name='Внутренний контракт')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('cost', models.FloatField(verbose_name='Цена')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='accounts.company', verbose_name='Компании')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AlterModelOptions(
            name='externalcontract',
            options={'verbose_name': 'Внешние договор', 'verbose_name_plural': 'Внешние договоры'},
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='control.application', verbose_name='Заявка')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='control.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Требование',
                'verbose_name_plural': 'Требования',
            },
        ),
        migrations.CreateModel(
            name='OrderPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Кол-во')),
                ('cost', models.FloatField(verbose_name='Цена')),
                ('contract', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.externalcontract', verbose_name='Внешний контракт')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='control.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_parts', to='control.providerproduct', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Часть заказа',
                'verbose_name_plural': 'Части заказов',
            },
        ),
    ]