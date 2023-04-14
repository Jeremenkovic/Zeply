# Zeply

-DESRIPTION

 The Crypto Address Generator project is a web application that allows users to generate unique cryptocurrency addresses for Bitcoin (BTC) and Ethereum (ETH).
 The application is built with Django, a Python web framework, and uses the Bit and Web3 libraries for BTC and ETH address generation, respectively.
 The API endpoints are exposed using Django REST framework. The project consists of a single app, crypto_addresses, which contains the models, serializers, and views necessary for generating and listing crypto addresses.
 The CryptoAddress model has three fields: cryptocurrency, address, and created_at.
 The CryptoAddressSerializer defines the serialization and deserialization behavior of the model, while the views define the API endpoints.
 The GenerateAddressView is responsible for generating new crypto addresses. When a new address is generated, it is saved to the database along with its corresponding cryptocurrency type.
 The ListAddressView simply lists all the addresses that have been generated so far.
 Finally, the RetrieveAddressView retrieves the details of a single crypto address by its ID.
 To use the application, a user can make a POST request to the generate_address endpoint with the desired cryptocurrency type in the request body.
 The API will then generate a new address and return it as a response. The list_addresses endpoint can be used to retrieve a list of all generated addresses, while the retrieve_address endpoint can be used to retrieve the details of a single address by its ID.

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
 Send a POST request with cryptocurrency parameter set to either BTC or ETH:
 curl -X POST -H "Content-Type: application/json" -d '{"cryptocurrency":"BTC"}' http://localhost:8000/api/generate_address/
 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 You should receive a JSON response with a new cryptocurrency address:
 {
    "id": 1,
    "cryptocurrency": "BTC",
    "address": "mo9xBiLdb94L7wvXZfpDRT6E4qatqoAncw"
}
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
To see list of addresses, go to http://localhost:8000/api/list_address/
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
To retrieve a specific address, go to http://localhost:8000/api/retrieve_address/<id>/, where <id> is the ID of the address you want to retrieve.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


-TESTING
To run the unit tests, simply run: python manage.py test
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

-SCREENSHOTS
<img width="1440" alt="Screen Shot 2023-04-14 at 12 38 20 PM" src="https://user-images.githubusercontent.com/102044657/232008657-b6a512d2-a49a-4b01-a0ba-7fcc2c0137c6.png">

<img width="1440" alt="Screen Shot 2023-04-14 at 12 38 46 PM" src="https://user-images.githubusercontent.com/102044657/232008702-7ea95e9e-f9c2-44c8-9b2a-14c43d0ecdbc.png">

<img width="1440" alt="Screen Shot 2023-04-14 at 1 59 04 AM" src="https://user-images.githubusercontent.com/102044657/231900908-85b6488d-63c1-46e2-a42e-ae524d61c52a.png">

