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
from cryptography.fernet import Fernet
from django.shortcuts import get_object_or_404

def encrypt_key(key: str) -> str:
    cipher_suite = Fernet(Fernet.generate_key())
    cipher_text = cipher_suite.encrypt(key.encode())
    return cipher_text.decode()

def decrypt_key(encrypted_key: str) -> str:
    cipher_suite = Fernet(Fernet.generate_key())
    plain_text = cipher_suite.decrypt(encrypted_key.encode())
    return plain_text.decode()


class GenerateAddressView(generics.CreateAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer

    def perform_create(self, serializer):
        crypto = self.request.data['cryptocurrency']
        address, encrypted_key = None, None

        if crypto == 'BTC':
            private_key = PrivateKeyTestnet()
            address = private_key.address
            encrypted_key = encrypt_key(private_key.to_hex())
        elif crypto == 'ETH':
            try:
                acct = Account.create()
                private_key = acct.key
                address = acct.address
                encrypted_key = encrypt_key(private_key.hex())
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif crypto == 'BCH':
            private_key = BCHKey()
            address = private_key.address
            encrypted_key = encrypt_key(private_key.to_hex())
        elif crypto == 'XRP':
            wallet = XRPWallet.create()
            private_key = wallet.private_key # Set private_key for XRP
            address = wallet.classic_address
            encrypted_key = encrypt_key(private_key)
        elif crypto == 'XLM':
           keypair = XLMKeypair.random()
           private_key = keypair.secret
           address = keypair.public_key
           encrypted_key = encrypt_key(private_key)
        else:
            return Response({"error": "Invalid cryptocurrency"}, status_code=status.HTTP_400_BAD_REQUEST)

        if address and encrypted_key:
            serializer.save(cryptocurrency=crypto, address=address, encrypted_private_key=encrypted_key)



class ListAddressView(generics.ListAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer

class RetrieveAddressView(generics.RetrieveAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer
