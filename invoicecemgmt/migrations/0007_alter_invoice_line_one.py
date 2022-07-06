# Generated by Django 4.0 on 2022-07-04 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventory_title'),
        ('invoicecemgmt', '0006_alter_invoice_line_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='line_one',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory', to_field='title'),
        ),
    ]
