from kmu_econ import app



# 使用路由 为URL 绑定视图函数
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
