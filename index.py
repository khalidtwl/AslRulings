import pickle
import random
import pandas as pd
from flask import Flask
from flask import render_template
from flask import Markup
app = Flask(__name__)

rulings = []


@app.route("/")
def landing():
    rulings = pickle.load(open( "asl_rulings_compiled.p", "rb" ))
    ruling = random.choice(rulings)
    return render_template('landing.html', ruling=ruling)


@app.route("/ruling/<int:ruling_id>")
def ruling(ruling_id):
    return 'ruling %s' % ruling_id
    return render_template('ruling.html', ruling_id=ruling_id)


@app.route("/search")
def search():
    full_data_table = pd.read_csv('Rulings Data/Full List-Table 1.csv')
    safe_table_html = Markup(full_data_table.to_html(table_id='rulingsTableMaster'))
    return render_template('search.html', table=safe_table_html)


@app.route("/howtouse")
def how_to_use():
    return render_template('howtouse.html')


@app.route('/about')
def about():
    return render_template('about.html')
