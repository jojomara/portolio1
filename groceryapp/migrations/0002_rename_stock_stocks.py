# Generated by Django 5.0.4 on 2024-08-12 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stock',
            new_name='Stocks',
        ),
    ]
