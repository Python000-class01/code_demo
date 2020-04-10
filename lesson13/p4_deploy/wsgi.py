from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def main():
    return 'hello'

if __name__ == '__main__':
    app.run()

