# imports
from flask import Flask
from dotenv import load_dotenv

# custom imports
from APICaller import get_characters

if __name__ == "__main__":
    get_characters()