from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-quote")
def get_quote():
    with open("static/data/quotes.json", "r") as f:
        quotes = json.load(f)
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(debug=True)
