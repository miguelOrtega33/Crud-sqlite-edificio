# Generated by Django 5.2.1 on 2025-06-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=500)),
                ('piso', models.PositiveIntegerField()),
            ],
        ),
    ]
