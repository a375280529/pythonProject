#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import numpy as nm
import requests
import json
import os
import configparser
import sys

def maopao(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def quzero(val):
    try:
        dex=val.index('.')
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

#读取原始单元格格式的excel
def readExcelRealGeShi(url):
    df = pd.read_excel(url, sheet_name=0, converters={'sw_jcxx_hy':str,'sw_jcxx_nsrztdm':str,'nsrsbh':str,'sw_jcxx_xzqh':str})
    list = []
    for i in range(len(df)):
        map = {}
        for name in df:
            if isinstance(df[name][i],str):
                map[name] = df[name][i]
            elif isinstance(df[name][i],datetime.datetime):
                map[name] = datetime.datetime.strftime(df[name][i],'%Y/%m/%d')
            elif isinstance(df[name][i], nm.integer):
                map[name] = int(df[name][i])
            elif isinstance(df[name][i], nm.floating):
                if str(df[name][i])=="nan":
                    map[name] = 0.0
                else:
                    map[name] = float(df[name][i])
            else:
                if str(df[name][i])=="nan":
                    map[name] = ''
                else:
                    map[name] = quzero(str(df[name][i]))
        list.append(map)
    return list

def getJsonForPostInterface(url,param,headers):
    result = {}
    r = requests.post(url,json=param, headers = headers)
    # 用自带的json把字符串转成字典
    try:
        dictinfo = json.loads(r.text)
        result["json"] = dictinfo
        result["code"] = r.status_code
        result["headers"] = r.headers
        result["cookies"] = r.cookies
    except:
        dictinfo = r.text
        result["json"] = dictinfo
        result["code"] = r.status_code
        result["headers"] = r.headers
        result["cookies"] = r.cookies
    return result

#读取ini配置文件数据
def getIni(ini):
    config = readini(ini)
    return config

# 读取配置文件的方法，ini为配置文件名称
def readini(ini):
    path = getIniPath() + ini
    config = configparser.ConfigParser()
    config.read(path,encoding="utf-8-sig")
    return config

# 获取配置文件相对路径
def getIniPath():
    # exepath = os.path.realpath(sys.executable)
    # endpath = exepath.split(exepath.split("\\")[-1])[0]
    # path=os.path.join(os.path.abspath('.'), endpath + "iniFile\\")
    path = os.path.dirname(os.path.abspath(__file__))
    path = path.split(path.split('\\')[-1])[0] + "iniFile" + "\\"
    return path