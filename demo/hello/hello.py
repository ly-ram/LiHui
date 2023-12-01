from flask import *

hello = Flask(__name__)


@hello.route('/')
def index():
    return "<h1>hello world</h1>"


@hello.route('/nihao')
@hello.route('/hellworld')
# 同一个视图被绑定多个路由
def helloworld():
    return "<h1>你好啊</h1>"


@hello.route('/greet/<name>')
#URL中可以包含变量，将传入app.route()的字符串称为URL规则，而不是URL
def greet(name):
    return '<h1> hello  {} </h1>'.format(name)
if __name__ == '__main__':
    hello.run(debug=True)
