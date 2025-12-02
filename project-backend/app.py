from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow browser calls from your frontend (localhost:5173, etc.)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask in Docker!"})
