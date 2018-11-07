from flask import Flask

#app = Flask(__name__) #创建1个Flask实例


@app.route('/')  #路由，处理URL和视图函数的关系
def hello_world():  #视图函数
    return 'Hello World!'


if __name__ == '__main__':
    app.run()  #启动socket
