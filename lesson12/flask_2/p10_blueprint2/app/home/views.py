from . import home

@home.route('/')
def index():
        return '<h1> page index </h1>'