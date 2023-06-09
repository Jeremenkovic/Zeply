# Generated by Django 4.2 on 2023-04-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_api', '0003_cryptoaddress_encrypted_private_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptoaddress',
            name='account_index',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cryptoaddress',
            name='derivation_path',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cryptoaddress',
            name='cryptocurrency',
            field=models.CharField(choices=[('BTC', 'Bitcoin'), ('ETH', 'Ethereum'), ('BCH', 'Bitcoin Cash'), ('XRP', 'Ripple'), ('XLM', 'Stellar')], max_length=10),
        ),
    ]
