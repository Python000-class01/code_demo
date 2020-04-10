from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key='key'
from forms import LoginForm
from flask import redirect, url_for,render_template, request
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            # 从db获取用户账号
            usr = 'admin'
            pwd = 'admin'

            if username == usr and password == pwd:
                return redirect(url_for("result"))
            else:
                return redirect(url_for("login"))
        else:
            return redirect(url_for("login"))
    return render_template('/home/login.html', form=form)

@app.route('/result')
def result():
    return  '登陆成功'


if __name__ == "__main__":
    app.run()
