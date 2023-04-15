#this file is used to generate fernet key for our security.
#THIS FILE SHOULD NOT BE IN HERE BUT I LEFT IT SO YOU CAN SEE HOW I WORKED ON THIS PROJECT
#This file should be ran seperately and only once to generate the key
#After generating in, I will store it in .env file THAT ALSO SHOULD NOT BE INCLUDED IN OUR REPO

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())