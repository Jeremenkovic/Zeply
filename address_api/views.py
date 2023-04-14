from typing import KeysView
from rest_framework import generics, status
from eth_account import Account
from requests import Response
from rest_framework import generics
from .models import CryptoAddress
from .serializers import CryptoAddressSerializer
from bit import PrivateKeyTestnet
from bitcash import Key as BCHKey
from xrpl.wallet import Wallet as XRPWallet
from stellar_sdk import Keypair as XLMKeypair
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
        elif crypto == 'BCH':
            private_key = BCHKey()
            address = private_key.address
            serializer.save(cryptocurrency=crypto, address=address)
        elif crypto == 'XRP':
            wallet = XRPWallet.create()
            address = wallet.classic_address
            serializer.save(cryptocurrency=crypto, address=address)
        elif crypto == 'XLM':
            keypair = XLMKeypair.random()
            address = keypair.public_key
            serializer.save(cryptocurrency=crypto, address=address)
        else:
            return Response({"error": "Invalid cryptocurrency"}, status=status.HTTP_400_BAD_REQUEST)




class ListAddressView(generics.ListAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer

class RetrieveAddressView(generics.RetrieveAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer
