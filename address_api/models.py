from django.db import models

class CryptoAddress(models.Model):
    CRYPTO_CHOICES = (
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('LTC', 'Litecoin'),
        ('BCH', 'Bitcoin Cash'),
        ('XRP', 'Ripple'),
        ('XLM', 'Stellar'),
    )
    id = models.AutoField(primary_key=True)
    cryptocurrency = models.CharField(max_length=10, choices=CRYPTO_CHOICES)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.cryptocurrency}: {self.address}"