# Generated by Django 4.2 on 2024-12-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_contacto_alter_producto_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
    ]
