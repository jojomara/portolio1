# Generated by Django 5.0.6 on 2024-08-27 00:10

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0004_rename_stock_price_stocks_issued_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('contacts', models.CharField(max_length=15)),
                ('amount_due', models.IntegerField()),
                ('sales_agent_name', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('produce_name', models.CharField(max_length=100)),
                ('produce_type', models.CharField(max_length=50)),
                ('tonnage', models.IntegerField()),
                ('dispatch_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='issued_quantity',
        ),
        migrations.AddField(
            model_name='sale',
            name='sales_agent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 3, 9, 15, 398910)),
        ),
        migrations.AddField(
            model_name='sale',
            name='stock_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocks',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 3, 9, 15, 398910)),
        ),
        migrations.AddField(
            model_name='stocks',
            name='stock_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]