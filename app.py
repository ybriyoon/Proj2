from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import data.getting_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/maps")
def maps():
    return render_template("maps.html")
@app.route('/load_data')
def scrape():
    data.getting_data.get_data()
    return redirect("/maps", code=302)

if __name__ == "__main__":
    app.run(debug=True)