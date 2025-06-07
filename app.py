from flask import Flask, Response
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = "https://webhook.site/8026044f-5d84-4804-ac4c-eaa0796bbd35"

@app.route("/")
def index():
    resp = requests.get(WEBHOOK_URL)
    return Response(resp.content, status=resp.status_code, content_type=resp.headers['Content-Type'])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

