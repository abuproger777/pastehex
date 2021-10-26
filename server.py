from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = "420bf172a6297fc6558b8a6075af347a83b124ccd8551b181a62bac7aefef321"
app.config["SESSION_COOKIE_HTTPONLY"] = False

@app.route("/")
def index():
    return render_template("index.html")

app.run("0.0.0.0", debug=True)