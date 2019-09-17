from flask import render_template
from twitoff import app

@app.route("/")

def home():
    return render_template('home.html')


@app.route("/about")

def pred():
    return render_template('about.html')