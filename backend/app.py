# imports
import time
import requests
from flask import Flask, jsonify
from flask_cors import CORS

# custom imports
from APICaller import get_characters

# flask app initialization
app: Flask = Flask(__name__)
CORS(app)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/all-characters')
def getCharacters():
    characters = get_characters()
    return jsonify({"characters": characters})

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
