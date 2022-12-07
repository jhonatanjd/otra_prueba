# Generated by Django 4.1.3 on 2022-11-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.AlterField(
            model_name='driver',
            name='vehicle_type',
            field=models.CharField(choices=[('Tractomula 3 troques', 'Tractomula 3 troques'), ('Minimula', 'Minimula'), ('Camion sencillo', 'Camion'), ('Tractomula 2 troques', 'Tractomula 2 troques'), ('Luv', 'Luv'), ('Pickup', 'Pickup'), ('Cuatro manos', 'Cuatro manos'), ('Doble troque', 'Doble troque'), ('Turbo', 'Turbo')], max_length=254, null=True),
        ),
    ]
