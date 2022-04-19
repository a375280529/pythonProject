#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import configparser
import random
import pandas as pd
from xml.dom.minidom import parse
import base64
import time

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
        if tname.hasAttribute("bname"):
            bsname=tname.getAttribute("bname")
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

#判断是否全是中文
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

#检验是否含有中文字符
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

#使用base64加密
def encryption_base64(str_cont):
    bytes_cont = str_cont.encode("utf-8")
    result = base64.b64encode(bytes_cont)
    return result


#解密base64格式的文本
def decrypt_base64(str_cont):
    result = base64.b64decode(str_cont).decode("utf-8")
    return result

#进度条，循环里面需要加上time.sleep(0.001)，percent是未转成百分比的小数,循环到最后的时候赋值为1（for i in range(10000);time.sleep(0.001);a=(i+1)/10000;progress(a)）
def progress(percent):
    if percent > 1:
        percent = 1
    res = int(50 * percent) * '>'
    print('\r[%-50s] %d%%' % (res, int(100 * percent)), end='')

#数组进行冒泡排序,从小到大
def maopao(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

#去除小数点末尾的0，val为str
def quzero(val):
    try:
        #dex=val.index('.')
        listv=val.split('.')
        lista=[]
        listb=[]
        biaoshi=0
        value=listv[0]
        ot=""
        for i in listv[1]:
            lista.append(i)
        for b in reversed(lista):
            if biaoshi==0:
                if b!="0":
                    listb.append(b)
                    biaoshi=1
                else:
                    pass
            else:
                listb.append(b)
        for c in reversed(listb):
            ot+=c
        if ot=="":
            pass
        else:
            value+="."+ot
        return value
    except:
        return val
