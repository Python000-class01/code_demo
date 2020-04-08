from flask import Blueprint

admin_list = Blueprint('admin', __name__) # 一个app里，蓝图名字不能重复

@admin_list.route('/news')
def do_admin():
    return '管理消息'