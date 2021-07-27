#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql as ms
import logging

def conMysql(host='',port='',user='',password='',database=''):
    # 连接数据库
    conn = ms.connect(host=host,port=port,user=user,password=password,database=database,charset='utf8')
    return conn

#查询多条数据返回所有数据值的List
def queryMysql(host,port,user,password,database, sql):
    conn = conMysql(host=host,port=port,user=user,password=password,database=database)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句
    result = cursor.execute(sql)
    # 使用fetchone()方法获取一条数据
    # data = cursor.fetchone()
    # 获取所有数据
    all_data = cursor.fetchall()
    # 获取部分数据，8条
    # many_data=cursor.fetchmany(8)
    #print(result.description)
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()
    return all_data

#查询出一条数据返回map
def queryMysqlReturnMap(host,port,user,password,database, sql):
    conn = conMysql(host=host,port=port,user=user,password=password,database=database)
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

#查询出多条数据并返回list
def queryMysqlAllReturnList(host,port,user,password,database, sql):
    conn = conMysql(host=host,port=port,user=user,password=password,database=database)
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


def updateMysql(host,port,user,password,database, sql):
    # 连接数据库
    conn = conMysql(host=host,port=port,user=user,password=password,database=database)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    try:
        # 使用execute方法执行SQL语句
        cursor.execute(sql)
        # 提交数据
        conn.commit()
        logging.info("插入或更新成功！")
    except:
        conn.rollback()
        logging.error("异常sql！")
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()

'''
@:param 数据库连接,存储过程名proname,
'''
#调用存储过程,传参数据库连接,存储过程名
def useMysqlPro(host,port,user,password,database,proname,inlist,outmap):
    conn = conMysql(host=host,port=port,user=user,password=password,database=database)
    cursor=conn.cursor()
    list=[]
    for inname in inlist:
        list.append(inname)
    for outname in outmap.keys():
        if outmap[outname]=="str":
            outname=cursor.var(ms.STRING)
            list.append(outname)
        elif outmap[outname]=="number":
            outname = cursor.var(ms.NUMBER)
            list.append(outname)
        elif outmap[outname]=="datetime":
            outname = cursor.var(ms.DATETIME)
            list.append(outname)
        elif outmap[outname] == "timestamp":
            outname = cursor.var(ms.TIMESTAMP)
            list.append(outname)
        elif outmap[outname] == "char":
            outname = cursor.var(ms.FIXED_CHAR)
            list.append(outname)
        elif outmap[outname] == "clob":
            outname = cursor.var(ms.CLOB)
            list.append(outname)
        elif outmap[outname] == "blob":
            outname = cursor.var(ms.BLOB)
            list.append(outname)
    try:
        result=cursor.callproc(proname,list)
        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    pass
    # sql="update djangochild_project set project_name='qwe' where id='2'"
    # result=updateMysql("localhost",3306,"zhangchuan","zhangchuan","dbtest",sql)
    # print(result)

