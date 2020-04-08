from . import home
from flask import render_template, redirect


@home.route('/')
def index():
        return redirect('/bootstrap')

@home.route('/bootstrap')
def bs():
        return render_template('home/home.html')