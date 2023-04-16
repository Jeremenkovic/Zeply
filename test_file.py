from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from address_api.models import CryptoAddress


class CryptoAddressTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    
    def test_generate_address_different_account_index(self):
        url = reverse('generate_address')
        data = {'account_index': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get('address'))
        self.assertIsNotNone(response.data.get('private_key'))

    def test_address_listing(self):
        CryptoAddress.objects.create(address='address1', private_key='private_key1')
        CryptoAddress.objects.create(address='address2', private_key='private_key2')

        url = reverse('address_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['address'], 'address1')
        self.assertEqual(response.data[1]['address'], 'address2')

    def test_address_details(self): 
        address_obj = CryptoAddress.objects.create(address='address1', private_key='private_key1')

        url = reverse('address_detail', args=[address_obj.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['address'], 'address1')
        self.assertEqual(response.data['private_key'], 'private_key1')

    def test_address_details_not_found(self):
        url = reverse('address_detail', args=[999])  # A non-existent address ID
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
