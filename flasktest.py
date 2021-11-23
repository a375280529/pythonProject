# -*- coding: utf-8 -*-
from flask import Flask,request,Response,jsonify
#werkzeug库可以判断文件名是否安全，例如防止文件名是../../../a.png
from werkzeug.utils import secure_filename
import json
import os
#内置变量__name__的值是字符串__main__ 。Flask类将这个参数作为程序名称。当然这个是可以自定义的
#Flask默认使用static目录存放静态资源，templates目录存放模板，这是可以通过设置参数更改的
app = Flask("myapp", static_folder="path1", template_folder="path2")

# 文件上传目录
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
# 支持的文件格式
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # 集合类型
#设置请求实体的大小
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB

# 判断文件名是否是我们支持的格式
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/hello')
def hello():
    #获取/hello
    print(request.path)
    #获取/hello和后面参数
    print(request.full_path)
    #获取url
    print(request.url)
    #获取所有参数
    print(dict(request.args))
    #获取参数值
    print(request.args.get("info"))
    #设置缺省值
    print(request.args.get("meiyouzhi","hello"))
    #获取多值的参数
    p=request.args.getlist("p")
    print(p)
    print(request.args.__str__())
    return str(p)

@app.route('/register', methods=['POST'])
def register():
    #请求头
    print(request.headers)
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    #print(request.json.get("nsrsbh","zxc").strip())  # 用户名
    print(request.headers.get("key","keys").strip())  # key
    return 'welcome'

@app.route('/add', methods=['POST'])
def add():
    result = {'sum': request.json['a'] + request.json['b']}
    resp=Response(json.dumps(result), mimetype='application/json')
    resp.headers.add('Server', 'python flask')
    return resp

@app.route('/addin', methods=['POST'])
def addin():
    result = {'sum': request.json['a'] + request.json['b']}
    #直接使用jsonify工具函数返回
    return jsonify(result)

@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image']
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        # 将文件保存到 static/uploads 目录，文件名同上传时使用的文件名
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'info is '+request.form.get('info', '')+'. success'
    else:
        return 'failed'


@app.route('/user/<username>')
def user(username):
    print(username)
    print(type(username))
    return 'hello ' + username


@app.route('/user/<username>/friends')
def user_friends(username):
    print(username)
    print(type(username))
    return 'hello ' + username+". They are your friends."

@app.route('/page/<int:num>')
def page(num):
    print(num)
    print(type(num))
    return 'hello world'+str(num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
