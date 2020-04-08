from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   # 使用模版和传值
   return render_template('index.html', text='Welcome')


if __name__ == '__main__':
   app.run(debug=True)

