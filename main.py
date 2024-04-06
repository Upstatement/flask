from flask import Flask, jsonify
import os
import chromadb

app = Flask(__name__)

client = chromadb.HttpClient(
    host=os.getenv('CHROMA_DB_HOST', 'chroma.railway.internal')
    settings=chromadb.config.Settings(chroma_client_auth_provider="chromadb.auth.token.TokenAuthClientProvider",
                                      chroma_client_auth_credentials=os.getenv('CHROMA_DB_AUTH_CREDENTIALS'))

client.heartbeat()  # this should work with or without authentication - it is a public endpoint

client.get_version()  # this should work with or without authentication - it is a public endpoint

client.list_collections()  # this is a protected endpoint and requires authentication


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
