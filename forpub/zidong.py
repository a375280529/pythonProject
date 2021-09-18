#!/usr/bin/python
# -*- coding: utf-8 -*-

import cx_Oracle as cx
import os
import configparser
import time
import sys

def conOracle(url):
    # 连接数据库
    conn = cx.connect(url)
    return conn

#查询出多条数据并返回list
def queryOracleAllReturnList(url, sql):
    conn = conOracle(url)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句
    result = cursor.execute(sql)
    rows = cursor.fetchall()
    list=[]
    fieldnames = [key[0] for key in cursor.description]
    if rows is None:
        pass
    else:
        for row in rows:
            mapresult = {}
            for i in range(len(fieldnames)):
                mapresult[fieldnames[i]] = row[i]
            list.append(mapresult)
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()
    return list

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

#查询出一条数据返回map
def queryOracleReturnMap(url, sql):
    conn = conOracle(url)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句
    result = cursor.execute(sql)
    rows = cursor.fetchone()
    mapresult = {}
    fieldnames = [key[0] for key in cursor.description]
    if rows is None:
        pass
    else:
        for i in range(len(fieldnames)):
            mapresult[fieldnames[i]] = rows[i]
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()
    return mapresult

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
    exepath = os.path.realpath(sys.executable)
    endpath = exepath.split(exepath.split("\\")[-1])[0]
    path = os.path.join(os.path.abspath('.'), endpath)
    return path

if __name__ == '__main__':
    print("执行中。。。")
    nsrsql="select NSRSBH,DBRMC,DBR_ZJHM from zx_lxrxx where bssf = 1 order by lrsj desc"
    ini=getIni("logger.ini")
    url = ini["callpro"]["callproConnectUsername"] + "/" + ini["callpro"]["callproConnectPassword"] + "@" + \
          ini["callpro"]["callproConnectIp"] + "/" + ini["callpro"]["callproConnectTable"]
    nsrresult=queryOracleAllReturnList(url, nsrsql)
    listallnsr=[]
    for nsrall in nsrresult:
        try:
            mapall={}
            nsrsbh=nsrall["NSRSBH"]
            applysql="SELECT T.APPLY_REQ_NO FROM (SELECT APPLY_REQ_NO FROM GS_BASE_INFO WHERE CREDIT_CODE = '%s' ORDER BY ESDATE DESC) T WHERE ROWNUM=1"%(nsrsbh)
            recordsql="SELECT T.RECORD_ID FROM (SELECT RECORD_ID FROM PR_HEAD_INFO WHERE NSRSBH = '%s' ORDER BY UPDATE_TIME DESC) T WHERE ROWNUM=1"%(nsrsbh)
            applyresult = queryOracleReturnMap(url, applysql)
            recordresult = queryOracleReturnMap(url, recordsql)
            mapall["NSRSBH"]=nsrall["NSRSBH"]
            mapall["DBRMC"] = nsrall["DBRMC"]
            mapall["DBR_ZJHM"] = nsrall["DBR_ZJHM"]
            mapall["APPLY_REQ_NO"] = applyresult["APPLY_REQ_NO"]
            mapall["RECORD_ID"] = recordresult["RECORD_ID"]
            listallnsr.append(mapall)
        except Exception as e:
            print(e)
            continue
    for ansr in listallnsr:
        inlist = []
        outmap = {}
        inlist.append(ansr["NSRSBH"])
        inlist.append(ansr["DBR_ZJHM"])
        inlist.append(ansr["DBRMC"])
        inlist.append(ansr["APPLY_REQ_NO"])
        inlist.append(ansr["RECORD_ID"])
        inlist.append(time.strftime('%Y-%m-%d'))
        outmap["SXED"] = "String"
        outmap["PREACCESS"] = "String"
        outmap["PREACCESSDESC"] = "String"
        # 调用存储过程
        result = usePro(url, "P_MX_HTYH", inlist, outmap)
        print("执行结果："+str(result))

    print("执行完成。。。")
    time.sleep(2)










