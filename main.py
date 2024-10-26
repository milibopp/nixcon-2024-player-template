from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)

app.run(port=os.getenv("PORT", 8080))
