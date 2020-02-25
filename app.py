from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    x = 2 + 2
    return "Hello World! {x}"

@app.route("/about")
def hello():
    return "About me"

@app.route("/books")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books)