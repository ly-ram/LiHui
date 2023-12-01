from flask import *

hello = Flask(__name__)


@hello.route()
def index():
    return "<h1>hello world</h1>"
