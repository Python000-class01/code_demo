from flask import Flask
import admin, news

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


app.register_blueprint(news.news_list)
app.register_blueprint(admin.admin_list, url_prefix='/admin')

if __name__ == "__main__":
    app.run(debug=True)