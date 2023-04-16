from django.db import models

class CryptoAddress(models.Model):
    CRYPTO_CHOICES = (
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('BCH', 'Bitcoin Cash'),
        ('XLM', 'Stellar'),
    )
    id = models.AutoField(primary_key=True)
    cryptocurrency = models.CharField(max_length=10, choices=CRYPTO_CHOICES)
    address = models.CharField(max_length=255)
    encrypted_private_key = models.CharField(max_length=255, default='')
    account_index = models.PositiveIntegerField(default=0)
    derivation_path = models.CharField(max_length=255, null=True)


    def __str__(self):
        return f"{self.cryptocurrency}: {self.address}"