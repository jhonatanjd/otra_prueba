# Generated by Django 4.1.3 on 2022-11-29 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_productos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='distribuidor',
        ),
        migrations.DeleteModel(
            name='tabla_prueba',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]