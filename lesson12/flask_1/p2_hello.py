from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return '<h1>hello world </h1>'

@app.route('/user/<name>') #通过get方式对url做处理
def user(name):
   return f'<h1> hello, {name}  ! </h1>'

if __name__ == '__main__':
   app.run(debug=True)

# cd day0409/1flask/
# export FLASK_APP=p2_hello.py
# $env:FLASK_APP = "hello.py"  # powershell
# set FLASK_APP=hello.py # cmd
# flask run --host=0.0.0.0
