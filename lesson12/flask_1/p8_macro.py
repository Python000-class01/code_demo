from flask import Flask, render_template, url_for, redirect
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
   return redirect('login')

@app.route('/login')
def on_login():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug=True)
