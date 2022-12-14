# Generated by Django 4.1.3 on 2022-11-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_registro_alter_driver_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='vehicle_type',
            field=models.CharField(choices=[('Minimula', 'Minimula'), ('Luv', 'Luv'), ('Doble troque', 'Doble troque'), ('Turbo', 'Turbo'), ('Pickup', 'Pickup'), ('Tractomula 2 troques', 'Tractomula 2 troques'), ('Camion sencillo', 'Camion'), ('Cuatro manos', 'Cuatro manos'), ('Tractomula 3 troques', 'Tractomula 3 troques')], max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='password',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='registro',
            name='username',
            field=models.CharField(max_length=254),
        ),
    ]
