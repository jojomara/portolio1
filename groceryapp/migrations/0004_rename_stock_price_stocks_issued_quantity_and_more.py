# Generated by Django 5.0.4 on 2024-08-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0003_sale_delete_sales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='stock_price',
            new_name='issued_quantity',
        ),
        migrations.RenameField(
            model_name='stocks',
            old_name='stock_name',
            new_name='item_name',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='stock_tonnage',
        ),
        migrations.AddField(
            model_name='stocks',
            name='total_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stocks',
            name='unit_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
