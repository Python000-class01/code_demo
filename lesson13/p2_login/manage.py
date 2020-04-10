from flask import Flask
from forms import LoginForm
from flask import redirect, url_for,render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config


# 使用flask_login 功能处理登陆后的session问题
from  flask_login import LoginManager, login_user, login_required
from  flask_login import current_user
login_manager = LoginManager()
app = Flask(__name__)

# 加载配置
app.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(app)

from models import *

# 绑定登陆管理
login_manager.init_app(app)

# 类似Django认证用户模型
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        # 验证form表单格式是否合法
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            # 从db获取用户账号
            usr = User.query.filter(User.username == username).one_or_none()
            # 判断用户
            if usr and usr.verify_password(password):
                
                # 处理session及其他
                login_user(usr, form.remeberme.data)
                return redirect(url_for("result"))
            else:
                return redirect(url_for("login"))
        else:
            from flask import flash
            flash('登陆失败')
    return render_template('/home/login.html', form=form)


@app.route('/result')
@login_required
def result():
    return  '登陆成功'

if __name__ == "__main__":
    app.run()
