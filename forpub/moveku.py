#!/usr/bin/python
# -*- coding: utf-8 -*-

import cx_Oracle as cx
import os
import configparser
import sys


def conOracle(url):
    # 连接数据库
    conn = cx.connect(url)
    return conn

#执行sql
def usesql(url, sql):
    biaoshi=0
    conn = conOracle(url)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句
    try:
        cursor.execute(sql)
    except Exception as e:
        biaoshi=1
        print("%s:执行异常"%(sql))
        print(e)
    finally:
        cursor.close()
        conn.close()
    return biaoshi

def updateOracle(url, sql,tablename):
    # 连接数据库
    conn = conOracle(url)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    try:
        # 使用execute方法执行SQL语句
        cursor.execute(sql)
        # 提交数据
        conn.commit()
        print("%s:数据插入成功" % (tablename))
    except:
        conn.rollback()
        print("%s:数据插入异常" % (tablename))
        print("%s:sql执行异常" % (sql))
    finally:
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()

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
    # path = os.path.dirname(os.path.abspath(__file__))
    # path = path.split(path.split('\\')[-1])[0] + "iniFile" + "\\"
    exepath = os.path.realpath(sys.executable)
    endpath = exepath.split(exepath.split("\\")[-1])[0]
    path = os.path.join(os.path.abspath('.'), endpath + "iniFile\\")
    return path

def readTxt(url):
    with open(url, "r", encoding="utf-8") as f:
        txt=f.readlines()
        return txt

class moveku():
    def __init__(self):
        self.ini = getIni("loggermove.ini")
        self.callpro=self.ini["callpro"]
        self.firstcallproConnectUsername = self.callpro["firstcallproConnectUsername"]
        self.firstcallproConnectPassword = self.callpro["firstcallproConnectPassword"]
        self.firstcallproConnectIp = self.callpro["firstcallproConnectIp"]
        self.firstcallproConnectTable = self.callpro["firstcallproConnectTable"]
        self.callproConnectUsername = self.callpro["callproConnectUsername"]
        self.callproConnectPassword = self.callpro["callproConnectPassword"]
        self.callproConnectIp = self.callpro["callproConnectIp"]
        self.callproConnectTable = self.callpro["callproConnectTable"]
        self.firsturl = self.firstcallproConnectUsername + "/" + self.firstcallproConnectPassword + "@" + self.firstcallproConnectIp + "/" + self.firstcallproConnectTable
        self.url=self.callproConnectUsername + "/" + self.callproConnectPassword + "@" + self.callproConnectIp + "/" + self.callproConnectTable
        self.txtpath=self.callpro["txtpath"]
        self.tablenamepath = self.callpro["tablenamepath"]
        self.table=""
        self.nsrsbh = ""

    def creatKu(self):
        kusql="create user %s identified by %s"%(self.callproConnectUsername,self.callproConnectPassword)
        biaoshi = usesql(self.firsturl, kusql)
        if biaoshi == 0:
            print("建库成功！")
        else:
            print("建库失败！")
        fudbasql = "grant dba to %s" % (self.callproConnectUsername)
        biaoshi = usesql(self.firsturl, fudbasql)
        if biaoshi == 0:
            print("赋权dba成功！")
        else:
            print("赋权dba失败！")
        selectsql = "grant select any table to %s" % (self.callproConnectUsername)
        biaoshi = usesql(self.firsturl, selectsql)
        if biaoshi == 0:
            print("赋权select any成功！")
        else:
            print("赋权select any失败！")
        fujobsql = "grant create job to %s" % (self.callproConnectUsername)
        biaoshi = usesql(self.firsturl, fujobsql)
        if biaoshi == 0:
            print("赋权job成功！")
        else:
            print("赋权job失败！")

    def connectdblink(self):
        dblinksql="create public database link %s connect to %s identified by %s using '%s'"%(self.callproConnectUsername,self.firstcallproConnectUsername,self.firstcallproConnectPassword,self.firstcallproConnectIp+"/"+self.firstcallproConnectTable)
        print("dblink创建中！")
        biaoshi=usesql(self.url,dblinksql)
        if biaoshi==0:
            print("dblink创建成功！")
        else:
            print("dblink创建失败！")

    def dropdblink(self):
        dropdblinksql = "drop public database link %s" % (self.callproConnectUsername)
        print("dblink删除中！")
        biaoshi=usesql(self.url, dropdblinksql)
        if biaoshi == 0:
            print("dblink删除成功！")
        else:
            print("dblink删除失败！")

    def readMoveTxt(self):
        movetxt=readTxt(self.txtpath)
        return movetxt

    def readTableNameTxt(self):
        moveTable=readTxt(self.tablenamepath)
        return moveTable

    def moveTable(self):
        movetablesql="create table %s as select * from %s @%s"%(self.table,self.table,self.callproConnectUsername)
        print(self.table)
        print("%s表建立中。。。"%(self.table))
        biaoshi=usesql(self.url, movetablesql)
        if biaoshi==0:
            print("%s表建立成功！"%(self.table))
        else:
            print("%s表建立失败！" % (self.table))

    def moveNsrsbhAll(self):
        bgdjsql = "insert into zx_bgdjxx select * from zx_bgdjxx@%s where nsrsbh in (%s)"%(self.callproConnectUsername,self.nsrsbh)
        jcajsql = "insert into zx_jcajxx select * from zx_jcajxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        lrbsql = "insert into zx_lrbxx select * from zx_lrbxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        lxrsql = "insert into zx_lxrxx select * from zx_lxrxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        nsrjcsql = "insert into zx_nsrjcxx select * from zx_nsrjcxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        sbsql = "insert into zx_sbxx select * from zx_sbxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        sbzssql = "insert into zx_sbzsxx select * from zx_sbzsxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        tzfsql = "insert into zx_tzfxx select * from zx_tzfxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        wfwzsql = "insert into zx_wfwzxx select * from zx_wfwzxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        zcfzbsql = "insert into zx_zcfzbxx select * from zx_zcfzbxx@%s where nsrsbh in (%s)" % (self.callproConnectUsername, self.nsrsbh)
        updateOracle(self.url,bgdjsql,"zx_bgdjxx")
        updateOracle(self.url, jcajsql, "zx_jcajxx")
        updateOracle(self.url, lrbsql, "zx_lrbxx")
        updateOracle(self.url, lxrsql, "zx_lxrxx")
        updateOracle(self.url, nsrjcsql, "zx_nsrjcxx")
        updateOracle(self.url, sbsql, "zx_sbxx")
        updateOracle(self.url, sbzssql, "zx_sbzsxx")
        updateOracle(self.url, tzfsql, "zx_tzfxx")
        updateOracle(self.url, wfwzsql, "zx_wfwzxx")
        updateOracle(self.url, zcfzbsql, "zx_zcfzbxx")

if __name__ == '__main__':
    ini = getIni("loggermove.ini")
    mbiaoshi = ini["callpro"]["mbiaoshi"]
    mk=moveku()
    if mbiaoshi == "0":
        mk.creatKu()
    mk.connectdblink()
    if mbiaoshi == "1":
        movetxt=mk.readMoveTxt()
        for val in movetxt:
            tablename=val.replace("\n","").strip()
            for tn in tablename.split(","):
                if tn.strip()!="":
                    mk.table=tn.strip()
                    mk.moveTable()
    if mbiaoshi=="2":
        movetablename = mk.readTableNameTxt()
        mk.nsrsbh = ""
        for valtable in movetablename:
            valnsr=valtable.replace("\n","").strip()
            for vn in valnsr.split(","):
                if vn.strip()!="":
                    mk.nsrsbh+="'"+vn.strip()+"',"
        mk.nsrsbh=mk.nsrsbh[:-1]
        mk.moveNsrsbhAll()
    mk.dropdblink()