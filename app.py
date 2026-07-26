from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return {
        "message": "Game Deal Finder API is running!"
    }


@app.route("/api")
def api():
    return {
        "message": "Welcome to the Game Deal Finder API!"
    }


if __name__ == "__main__":
    app.run(debug=True)