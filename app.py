from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import data.getting_data
import scrape_data 

app = Flask(__name__)
app.static_folder = 'templates/static'

mongo = PyMongo(app, uri="mongodb://localhost:27017/women_app")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/maps")
def maps():
    return render_template("maps.html")

@app.route("/timeline_with_data")
def timeline_with_data():
    world_data = mongo.db.world_data.find_one()
    return render_template("timeline2.html", world_data=world_data)

@app.route("/timeline/indoor")
def timeline_indoor():
    world_data = mongo.db.world_data.find_one()
    return render_template("indoor.html", world_data=world_data)

@app.route("/timeline/outdoor")
def timeline_outdoor():
    world_data = mongo.db.world_data.find_one()
    return render_template("outdoor.html", world_data=world_data)

@app.route('/load_data')
def scrape():
    # data.getting_data.get_data()
    world_data = mongo.db.world_data
    world_info = scrape_data.scrape()
    world_data.update({}, world_info, upsert=True)
    return redirect("/timeline_with_data", code=302)


@app.route("/plots")
def plots():
    return render_template("plots.html")


if __name__ == "__main__":
    app.run(debug=True)