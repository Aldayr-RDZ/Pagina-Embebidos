# Generated by Django 3.2 on 2021-05-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('idAlarma', models.UUIDField(primary_key=True, serialize=False)),
                ('estadoAlarma', models.BooleanField()),
            ],
        ),
    ]
