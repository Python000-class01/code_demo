from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index4.html')

@app.route('/otherurl')
def other():
   return 'url_for other function'


# 变量规则
@app.route('/userid/<int:uid>')
def user(uid):
   return f'uid : {uid}'

@app.route('/url1')
@app.route('/url2/')
def url():
   return 'test multiurl'


# 也能支持POST请求
from flask import request
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
#  https://dormousehole.readthedocs.io/en/latest/quickstart.html#id6



if __name__ == '__main__':
   app.run(debug=True)
