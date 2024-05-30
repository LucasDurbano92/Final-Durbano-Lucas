# Generated by Django 5.0.6 on 2024-05-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Varillas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='contacto',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='varilla',
            name='nombre',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='nombre',
            field=models.PositiveIntegerField(editable=False, unique=True),
        ),
    ]
