# Generated by Django 4.1.3 on 2022-12-04 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_delete_distribuidor_delete_tabla_prueba_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='productos',
        ),
    ]
