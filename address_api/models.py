from django.db import models

class CryptoAddress(models.Model):
    id = models.AutoField(primary_key=True)
    cryptocurrency = models.CharField(max_length=10)
    address = models.CharField(max_length=255)