# Generated by Django 4.2 on 2023-04-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cryptocurrency', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
