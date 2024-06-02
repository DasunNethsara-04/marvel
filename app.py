# imports
from flask import Flask, render_template
from dotenv import load_dotenv

# custom imports
from APICaller import get_characters

# flask app initialization
app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # get_characters()
    app.run(host="localhost", port=8080, debug=True)