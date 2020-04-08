from flask import Flask, render_template, url_for
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index6.html')

@app.route('/about')
def about():
   return 'about'

@app.template_test('current_link')
def current_link(link):
    return link == request.path

if __name__ == '__main__':
   app.run(debug=True)
