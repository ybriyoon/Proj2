from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def index():
    return


if __name__ == "__main__":
    app.run(debug=True)