# Generated by Django 5.0.6 on 2024-05-31 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Varillas', '0002_color_varilla_materiales_passpartou_vidrio_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cliente',
            unique_together={('nombre', 'apellido', 'contacto')},
        ),
    ]
