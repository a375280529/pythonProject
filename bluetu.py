# -*- coding: utf-8 -*-

from flask import Blueprint,Flask,jsonify

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