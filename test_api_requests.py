import unittest
import requests

class AddressApiRequestsTests(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000'

    def test_generate_btc_address(self):
        btc_data = {"cryptocurrency": "BTC"}
        btc_response = requests.post(f'{self.base_url}/api/generate_address/', data=btc_data)
        self.assertEqual(btc_response.status_code, 201)
        btc_response_data = btc_response.json()
        self.assertEqual(btc_response_data['cryptocurrency'], 'BTC')
        self.assertIsNotNone(btc_response_data['address'])

    def test_generate_eth_address(self):
        eth_data = {"cryptocurrency": "ETH"}
        eth_response = requests.post(f'{self.base_url}/api/generate_address/', data=eth_data)
        self.assertEqual(eth_response.status_code, 201)
        eth_response_data = eth_response.json()
        self.assertEqual(eth_response_data['cryptocurrency'], 'ETH')
        self.assertIsNotNone(eth_response_data['address'])

    def test_list_addresses(self):
        list_response = requests.get(f'{self.base_url}/api/list_address/')
        self.assertEqual(list_response.status_code, 200)
        list_response_data = list_response.json()
        self.assertIsInstance(list_response_data, list)

    def test_retrieve_address_by_id(self):
        # First, create an address to retrieve
        btc_data = {"cryptocurrency": "BTC"}
        btc_response = requests.post(f'{self.base_url}/api/generate_address/', data=btc_data)
        btc_response_data = btc_response.json()

        # Retrieve the address by ID
        retrieve_response = requests.get(f'{self.base_url}/api/retrieve_address/{btc_response_data["id"]}/')
        self.assertEqual(retrieve_response.status_code, 200)
        retrieve_response_data = retrieve_response.json()

        # Verify the retrieved address data
        self.assertEqual(retrieve_response_data['id'], btc_response_data['id'])
        self.assertEqual(retrieve_response_data['cryptocurrency'], btc_response_data['cryptocurrency'])
        self.assertEqual(retrieve_response_data['address'], btc_response_data['address'])

if __name__ == "__main__":
    unittest.main()
