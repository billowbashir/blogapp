from flask import render_template, url_for,redirect
from . import main




@main.route('/')
def index():
    return render_template('index.html')
