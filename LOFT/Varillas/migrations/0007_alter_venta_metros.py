# Generated by Django 5.0.6 on 2024-05-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Varillas', '0006_rename_cantidad_venta_metros_remove_venta_varilla_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='Metros',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]