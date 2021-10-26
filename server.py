import sqlite3
from flask import Flask, render_template, g


app = Flask(__name__)
app.config["SESSION_COOKIE_HTTPONLY"] = False

def get_db():
        db = getattr(g, "_database", None)
        if db is None:
            db = g._database = sqlite3.connect("pastehex.db")
        return db
    
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template("index.html")

app.run("0.0.0.0", debug=True)
