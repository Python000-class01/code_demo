from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# cd day0409/flask_1/
# flask run
# 微框架 灵活
