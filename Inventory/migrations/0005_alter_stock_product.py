# Generated by Django 4.1.6 on 2023-02-11 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_remove_order_date_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product'),
        ),
    ]
