# Generated by Django 4.1.3 on 2022-12-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(choices=[('medellin', 'medellin'), ('bogota', 'bogota'), ('barranquilla', 'barranquilla'), ('cali', 'cali')], max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='productos',
        ),
    ]