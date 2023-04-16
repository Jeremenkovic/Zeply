import os
from rest_framework import generics, status
from eth_account import Account
from requests import Response
from rest_framework import generics
from .models import CryptoAddress
from .serializers import CryptoAddressSerializer
from bit import PrivateKeyTestnet
from bitcash import Key as BCHKey
#from xrpl.wallet import Wallet as XRPWallet
from stellar_sdk import Keypair as XLMKeypair
from cryptography.fernet import Fernet
from django.shortcuts import get_object_or_404
from bip32 import BIP32
from mnemonic import Mnemonic
#from xrpl import Wallet as XRPWallet
from stellar_base.keypair import Keypair as XLMKeypair

FERNET_KEY = os.environ.get('FERNET_KEY')
if FERNET_KEY is None:
    raise ValueError("Fernet key not found in environment variables")

cipher_suite = Fernet(FERNET_KEY)

def encrypt_key(key: str) -> str:
    cipher_text = cipher_suite.encrypt(key.encode())
    return cipher_text.decode()

def decrypt_key(encrypted_key: str) -> str:
    plain_text = cipher_suite.decrypt(encrypted_key.encode())
    return plain_text.decode()

def generate_hd_wallet_address(crypto, seed_phrase, account_index):
    bip32_wallet = BIP32.from_seed(Mnemonic.to_seed(seed_phrase))
    if crypto == 'BTC':
        # Derivation path for Bitcoin
        path = f"m/44'/0'/0'/{account_index}"
    elif crypto == 'ETH':
        # Derivation path for Ethereum
        path = f"m/44'/60'/0'/0/{account_index}"
    else:
        raise ValueError("Unsupported cryptocurrency for HD wallet")

    child_key = bip32_wallet.get_privkey_from_path(path)
    
    if crypto == 'BTC':
        private_key = PrivateKeyTestnet.from_hex(child_key)
        address = private_key.address
    elif crypto == 'ETH':
        private_key = Account.from_key(child_key)
        address = private_key.address

    encrypted_key = encrypt_key(child_key)

    return address, encrypted_key

class GenerateAddressView(generics.CreateAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer

    def perform_create(self, serializer):
        crypto = self.request.data['cryptocurrency']
        seed_phrase = self.request.data.get('seed_phrase', None)
        account_index_value = self.request.data.get('account_index', 0)
        account_index = int(account_index_value) if account_index_value != '' else 0
        address, encrypted_key = None, None

        if seed_phrase:
            try:
                address, encrypted_key = generate_hd_wallet_address(crypto, seed_phrase, account_index)
                serializer.save(cryptocurrency=crypto, address=address, encrypted_private_key=encrypted_key, account_index=account_index)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
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

            elif crypto == 'XLM':
                keypair = XLMKeypair.random()
                private_key = keypair.seed()
                address = keypair.address().decode()
                encrypted_key = encrypt_key(private_key)
            else:
                return Response({"error": "Invalid cryptocurrency"}, status=status.HTTP_400_BAD_REQUEST)

            if address and encrypted_key:
                serializer.save(cryptocurrency=crypto, address=address, encrypted_private_key=encrypted_key)
class ListAddressView(generics.ListAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer

class RetrieveAddressView(generics.RetrieveAPIView):
    queryset = CryptoAddress.objects.all()
    serializer_class = CryptoAddressSerializer
