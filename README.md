# Zeply

-DESRIPTION

 The Crypto Address Generator project is a web application that allows users to generate unique cryptocurrency addresses and multiple currencies per one user for Bitcoin (BTC), Ethereum (ETH) and BitcoinCash (BCH).
 The application is built with Django and Postgress as database that is encrypted with FERNET_KEY, see fernet.py and .env file in the repo for more details PLEASE. Encryption is done in address_api/views.py.
 The API endpoints are exposed using Django REST framework.
 The CryptoAddressSerializer defines the serialization and deserialization behavior of the model, while the views define the API endpoints.
 The GenerateAddressView is responsible for generating new crypto addresses. When a new address is generated, it is saved to the database along with its corresponding cryptocurrency type.
 The ListAddressView simply lists all the addresses that have been generated so far.
 Finally, the RetrieveAddressView retrieves the details of a single crypto address by its ID.
 To use the application, a user NEEDS to make a POST request to the generate_address endpoint with the desired cryptocurrency type in the request body, if you dont specify account user, it will be set 0 as default.
 The API will then generate a new address and encrypted private key and return it as a response. The list_addresses endpoint can be used to retrieve a list of all generated addresses, while the retrieve_address endpoint can be used to retrieve the details of a single address by its ID.

-INSTALATION

You should have installed Python3 and Postgress on your system.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 Clone the repository: git clone https://github.com/yourusername/zeply.git
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 Install the dependencies: pip/pip3 install -r requirements.txt
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 Migrate the database: python manage.py migrate
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

-RUNNING

 Start your Postgress server: brew services start postgresql@13
 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 Start the development server: python/python3 manage.py runserver
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 Send a POST request with cryptocurrency parameter set to either BTC or ETH or BCH:
 curl -X POST -H "Content-Type: application/json" -d '{"cryptocurrency":"BTC"}' http://localhost:8000/api/generate_address/
 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 You should receive a JSON response with a new cryptocurrency address:
 {
     "id": 53,
    "cryptocurrency": "BCH",
    "address": "bitcoincash:qphvkhh6cwhszyhqltxzzs55tv0ufexdru3qqkmlll",
    "encrypted_private_key": "gAAAAABkPE_lJliK5mzBVBSohcR-814TldwiIPK71pSk72eRgBL1gfeM2hazNL4ML-J8NAoBDvBv0mWIRCOtGbxGAxFQ4-    b4CnijjtkL75KbF7ONKA8jWLDcox_qvJLw5i6JEKoDD6w_o8Tt8GeDvczVMoH3MQI2_TzBGaIsrDyjT4htWFlzYHg=",
    "account_index": 3
}
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
To see list of addresses, go to http://localhost:8000/api/list_address/
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
To retrieve a specific address, go to http://localhost:8000/api/retrieve_address/<id>/, where <id> is the ID of the address you want to retrieve.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


-TESTING

To run the unit tests, simply run: python3 manage.py test or  python3 manage.py test_api_requests
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

-SCREENSHOTS
 <img width="1440" alt="Screen Shot 2023-04-16 at 10 41 15 PM" src="https://user-images.githubusercontent.com/102044657/232338035-1a85bef3-8fac-4487-9158-561c9c2e338a.png">


<img width="1440" alt="Screen Shot 2023-04-14 at 12 38 46 PM" src="https://user-images.githubusercontent.com/102044657/232008702-7ea95e9e-f9c2-44c8-9b2a-14c43d0ecdbc.png">

<img width="1440" alt="Screen Shot 2023-04-16 at 10 49 00 PM" src="https://user-images.githubusercontent.com/102044657/232338411-135c883d-6bf0-4374-9504-39cbc4296568.png">

