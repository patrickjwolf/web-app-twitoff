from flask import Flask

# app.py

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World!"

