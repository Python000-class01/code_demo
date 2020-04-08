from flask import Blueprint

news_list = Blueprint('news', __name__) # news是蓝图的名字

@news_list.route('/news')
def do_news():
    return '滚动新闻'