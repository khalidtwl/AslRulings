import pickle
import random
from flask import Flask
from flask import render_template
app = Flask(__name__)

rulings = []


@app.route("/")
def landing():
    rulings = pickle.load(open( "asl_rulings_compiled.p", "rb" ))
    ruling = random.choice(rulings)
    return render_template('landing.html', ruling=ruling)


@app.route("/ruling/<int:ruling_id>")
def ruling():
    ruling


@app.route("/search")
def search():
    return 'Search page is under construction!'


@app.route("/howtouse")
def how_to_use():
    return 'How to use is under construction!'


@app.route('/about')
def about():
    return 'Welcome to the About page!\nEminent Rulings Scholar: Mr. Shahawy\nIllustrious Website Puppetmaster: Mr. Tawil'

