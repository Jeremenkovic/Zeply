import requests

base_url = 'http://127.0.0.1:8000'

# Test generating a Bitcoin address
btc_data = {"cryptocurrency": "BTC"}
btc_response = requests.post(f'{base_url}/api/generate_address/', data=btc_data)
print("BTC response status:", btc_response.status_code)
print("BTC response data:", btc_response.json())

# Test generating an Ethereum address
eth_data = {"cryptocurrency": "ETH"}
eth_response = requests.post(f'{base_url}/api/generate_address/', data=eth_data)
print("ETH response status:", eth_response.status_code)
print("ETH response data:", eth_response.json())
