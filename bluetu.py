# -*- coding: utf-8 -*-

from flask import Blueprint,Flask,jsonify,request

lantu=Blueprint('lantu',__name__)


@lantu.route("/hello/post",methods=["POST"])
def hellopost():
    print("hellopost")
    return "hellopost"


@lantu.route("/hello/get",methods=["GET"])
def helloget():
    print("helloget")
    return "helloget"

@lantu.route("/hello/post/get",methods=["POST","GET"])
def hellopostget():
    print("hellopostget")
    return "hellopostget"

@lantu.route('/register', methods=['POST'])
def register():
    #请求头
	print(request.headers)
	print(123321)
	print(request.headers.get("-Api-Name"))
	# print(request.form)
    # print(request.form['name'])
    # print(request.form.get('name'))
    # print(request.form.getlist('name'))
    # print(request.form.get('nickname', default='little apple'))
    # #print(request.json.get("nsrsbh","zxc").strip())  # 用户名
    # print(request.headers.get("key","keys").strip())  # key
	return 'welcome'