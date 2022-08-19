# Generated by Django 4.0.6 on 2022-08-19 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('tipo_operacion', models.TextField()),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('ID_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cuentas.cuenta')),
            ],
            options={
                'db_table': 'Movimientos',
            },
        ),
    ]
