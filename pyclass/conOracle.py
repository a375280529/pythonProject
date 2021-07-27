#!/usr/bin/python
# -*- coding: utf-8 -*-

import cx_Oracle as cx
import logging

def conOracle(url):
    # 连接数据库
    conn = cx.connect(url)
    return conn

#查询多条数据返回所有数据值的List
def queryOracle(url, sql):
    conn = conOracle(url)
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


def updateOracle(url, sql):
    # 连接数据库
    # "jrwz2_zx/jrwz2_zx@192.168.81.41:1521/emserver"
    conn = conOracle(url)
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
@:param 数据库连接url,存储过程名proname,
'''
#调用存储过程,传参数据库连接url,存储过程名
def usePro(url,proname,inlist,outmap):
    con=conOracle(url)
    cursor=con.cursor()
    list=[]
    for inname in inlist:
        list.append(inname)
    for outname in outmap.keys():
        if outmap[outname]=="str":
            outname=cursor.var(cx.STRING)
            list.append(outname)
        elif outmap[outname]=="number":
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

if __name__ == '__main__':
    pass
    # sql="select t.sw_bg_bsry_01m,t.* from T_JC_ZB t where t.nsrsbh='440100593700191'"
    # result=queryOracleReturnMap("vz_bz4/vz_bz4@192.168.85.81:1521/emserver",sql)
    # print(result)

