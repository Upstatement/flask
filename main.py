from flask import Flask, jsonify
import os
import chromadb

app = Flask(__name__)


db = chromadb.HttpClient(host=os.getenv('CHROMA_DB_HOST', 'chroma.railway.internal'))

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
