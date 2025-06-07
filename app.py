from flask import Flask, redirect
import os

app = Flask(__name__)

WEBHOOK_URL = https://webhook.site/8026044f-5d84-4804-ac4c-eaa0796bbd35

@app.route(/)
def index():
    return redirect(WEBHOOK_URL, code=302)

if __name__ == __main__:
    port = int(os.environ.get(PORT, 8080))  # Railway uses dynamic ports
    app.run(host=0.0.0.0, port=port)

