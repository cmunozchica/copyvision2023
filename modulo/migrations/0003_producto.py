# Generated by Django 4.1.7 on 2023-03-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0002_alter_trabajo_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categorias', models.CharField(choices=[('PAPELERIA', 'PAPELERIA'), ('PAPEL', 'PAPEL'), ('PLOTTER', 'PLOTTER'), ('PUBLICIDAD', 'PUBLICIDAD'), ('VARIOS', 'VARIOS')], max_length=20)),
                ('precio', models.FloatField()),
                ('cantidad', models.FloatField()),
                ('disponibilidad', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
