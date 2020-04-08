from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index5.html')

@app.route('/about')
def about():
   return 'about'

if __name__ == '__main__':
   app.run(debug=True)
