#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import cx_Oracle as cx
import datetime
import os
import configparser
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

#读取ini配置文件数据
def getIni(ini):
    config = readini(ini)
    return config

def conOracle(url):
    # 连接数据库
    conn = cx.connect(url)
    return conn

def updateOracle(url, sql):
    # 连接数据库
    conn = conOracle(url)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    try:
        # 使用execute方法执行SQL语句
        cursor.execute(sql)
        # 提交数据
        conn.commit()
    except:
        conn.rollback()
        print("sql异常"+sql)
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()

#调用存储过程,传参数据库连接url,存储过程名
def usePro(url,proname,inlist,outmap):
    con=conOracle(url)
    cursor=con.cursor()
    list=[]
    for inname in inlist:
        list.append(inname)
    for outname in outmap.keys():
        if outmap[outname]=="String":
            outname=cursor.var(cx.STRING)
            list.append(outname)
        elif outmap[outname]=="Float":
            outname = cursor.var(cx.NUMBER)
            list.append(outname)
        elif outmap[outname]=="datetime":
            outname = cursor.var(cx.DATETIME)
            list.append(outname)
        elif outmap[outname] == "timestamp":
            outname = cursor.var(cx.TIMESTAMP)
            list.append(outname)
        elif outmap[outname] == "char":
            outname = cursor.var(cx.FIXED_CHAR)
            list.append(outname)
        elif outmap[outname] == "clob":
            outname = cursor.var(cx.CLOB)
            list.append(outname)
        elif outmap[outname] == "blob":
            outname = cursor.var(cx.BLOB)
            list.append(outname)
    try:
        result=cursor.callproc(proname,list)
        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

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

#读取excel的所有sheet
def readExcelSheet(url):
    sheet = pd.read_excel(url, sheet_name=None, converters={'nsrsbh':str})
    listall=[]
    for va in sheet.values():
        va = va.to_dict(orient='records')
        list = []
        for i in range(len(va)):
            map = {}
            for name in va[i].keys():
                if isinstance(va[i][name], str):
                    map[name] = va[i][name]
                elif isinstance(va[i][name], datetime.datetime):
                    map[name] = datetime.datetime.strftime(va[i][name], '%Y/%m/%d')
                elif isinstance(va[i][name], float):
                    if str(va[i][name]) == "nan":
                        map[name] = str(None)
                    else:
                        map[name]=str(va[i][name])
                    #map[name]='{:g}'.format(va[i][name])
                else:
                    if str(va[i][name]) == "nan":
                        map[name] = str(None)
                    else:
                        map[name] = str(va[i][name])
            list.append(map)
        listall.append(list)
    return listall

