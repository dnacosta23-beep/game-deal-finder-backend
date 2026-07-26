from flask import Flask
from flask_cors import CORS

from routes.deals import deals_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(deals_bp)


@app.route("/")
def home():
    return {
        "message": "Welcome to the Game Deal Finder API!"
    }


if __name__ == "__main__":
    app.run(debug=True)