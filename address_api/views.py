from typing import KeysView
from rest_framework import generics, status
from eth_account import Account
from requests import Response
from rest_framework import generics
from .models import CryptoAddress
from .serializers import CryptoAddressSerializer
from bit import PrivateKeyTestnet
from django.shortcuts import get_object_or_404

class GenerateAddressView(generics.CreateAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer

    def perform_create(self, serializer):
        crypto = self.request.data['cryptocurrency']
        if crypto == 'BTC':
            private_key = PrivateKeyTestnet()
            address = private_key.address
            serializer.save(cryptocurrency=crypto, address=address)
        
        elif crypto == 'ETH':
            try:
                acct = Account.create()
                address = acct.address
                serializer.save(cryptocurrency=crypto, address=address)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListAddressView(generics.ListAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer

class RetrieveAddressView(generics.RetrieveAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer
