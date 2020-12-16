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

@app.route("/maps_with_data")
def maps_with_data():
    world_data = mongo.db.world_data.find_one()
    return render_template("maps2.html", world_data=world_data)

@app.route('/load_data')
def scrape():
    # data.getting_data.get_data()
    world_data = mongo.db.world_data
    world_info = scrape_data.scrape()
    world_data.update({}, world_info, upsert=True)
    return redirect("/other", code=302)


@app.route("/plots")
def plots():
    return render_template("plots.html")


@app.route("/timeline")
def timeline():
    return render_template("timeline.html")




if __name__ == "__main__":
    app.run(debug=True)