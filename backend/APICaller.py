# imports
import os
import pprint
import requests
import hashlib
import time
import json
from dotenv import load_dotenv

# load all the environment variables into the program
load_dotenv()

# Your Marvel API keys
public_key = os.getenv("PUBLIC_KEY")
private_key = os.getenv("PRIVATE_KEY")

# Function to create the required hash
def create_hash(ts, private_key, public_key) -> str:
    to_hash = ts + private_key + public_key
    hash_value = hashlib.md5(to_hash.encode()).hexdigest()
    return hash_value

# Function to get characters from Marvel API
def get_characters():
    base_url = 'http://gateway.marvel.com/v1/public/characters'
    ts = str(time.time())
    hash_value = create_hash(ts, private_key, public_key)
    params = {
        'apikey': public_key,
        'ts': ts,
        'hash': hash_value
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json().get('data', {}).get('results', [])
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")