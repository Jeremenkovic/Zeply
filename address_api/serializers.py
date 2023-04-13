from rest_framework import serializers
from .models import CryptoAddress

class CryptoAddressSerializer(serializers.ModelSerializer):
    address = serializers.CharField(read_only=True)

    class Meta:
        model = CryptoAddress
        fields = ['id', 'cryptocurrency', 'address']
