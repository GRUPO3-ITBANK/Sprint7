# Generated by Django 4.0.6 on 2022-08-19 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0007_remove_cliente_id_usuario'),
        ('Login', '0003_alter_myuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='id_cliente',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Clientes.cliente'),
            preserve_default=False,
        ),
    ]