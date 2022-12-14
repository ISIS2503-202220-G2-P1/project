# Generated by Django 4.1.1 on 2022-09-30 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc', models.TextField()),
                ('nombre', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc', models.TextField()),
                ('nombre', models.TextField()),
                ('email', models.TextField()),
                ('empresa', models.TextField()),
                ('informacion_personal', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=3, max_digits=20)),
                ('plazo_meses', models.IntegerField()),
                ('urlDocumentos', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditos.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.TextField()),
                ('analista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditos.analista')),
            ],
        ),
    ]
