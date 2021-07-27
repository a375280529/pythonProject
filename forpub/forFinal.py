#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import configparser
import random
import pandas as pd
from xml.dom.minidom import parse

# 获取配置文件相对路径
def getIniPath():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path.split(path.split('\\')[-1])[0] + "iniFile" + "\\"
    return path


# 读取配置文件的方法，ini为配置文件名称
def readini(ini):
    path = getIniPath() + ini
    config = configparser.ConfigParser()
    config.read(path,encoding="utf-8-sig")
    return config


# 获取日志文件相对路径
def getLogPath():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path.split(path.split('\\')[-1])[0] + "logFile" + "\\"
    return path

#随机数
def haveIntRondom():
    top=random.randint(10000000000, 99999999999)
    return top

#读取ini配置文件数据
def getIni(ini):
    config = readini(ini)
    return config

#解决乱码
def statement(value):
    data = value.encode("utf-8").decode("utf-8")
    return data

#解决网页返回信息乱码
def statementPage(value):
    data=value.encode("raw_unicode_escape").decode()
    return data

#返回xml根节点
def readXml():
    domTree=parse(os.path.abspath(os.path.join(os.getcwd(), ".."))+"/xmlFile/xmlfile.xml")
    # 文档根元素
    rootNode = domTree.documentElement
    return rootNode

#根据name读取xml中不同环境的数据库信息
def getXmlNode(name):
    map={}
    node=readXml()
    print(node.nodeName)
    tagname=node.getElementsByTagName("name")
    for tname in tagname:
        if tname.hasAttribute("name"):
            bsname=tname.getAttribute("name")
            if bsname==name:
                connectname=tname.getElementsByTagName("connectname")[0].childNodes[0].data
                connectpassword = tname.getElementsByTagName("connectpassword")[0].childNodes[0].data
                connectip = tname.getElementsByTagName("connectip")[0].childNodes[0].data
                dbname = tname.getElementsByTagName("dbname")[0].childNodes[0].data
                map["connectname"]=connectname
                map["connectpassword"] = connectpassword
                map["connectip"] = connectip
                map["dbname"] = dbname
                return map

#读取excel所有sheet
def readAllExcelSheet():
    sheet = pd.read_excel("E:\\test\\newgo.xlsx", sheet_name=None)
    #所有sheet的名称
    for j in sheet.keys():
        print(j)
    #每个sheet中所有数据信息
    for j1 in sheet.values():
        j1 = j1.to_dict(orient='records')
        print(j1)
    #sheet名称与数据信息键值对形式
    for k, v in sheet.items():
        v = v.to_dict(orient='records')
        print(k, v)
