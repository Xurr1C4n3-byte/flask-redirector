from flask import Flask, Response
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = "https://webhook.site/dbe4edad-666e-4b5a-badf-424f4b3a4e09"

@app.route("/")
def index():
    resp = requests.get(WEBHOOK_URL)
    return Response(resp.content, status=resp.status_code, content_type=resp.headers['Content-Type'])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

