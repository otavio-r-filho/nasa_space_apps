from src import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/humanitary_index')
def humanitary_index():
    return render_template('humanitary_index.html')