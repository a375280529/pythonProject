#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import pymysql as ms
import logging

def conMysql(host='',port='',user='',password='',database=''):
    # 连接数据库
    conn = ms.connect(host=host,port=int(port),user=user,password=password,database=database,charset='utf8')
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
            mapresult[str(fieldnames[i]).upper()] = rows[i]
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
                mapresult[str(fieldnames[i]).upper()] = row[i]
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
    finally:
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()

'''
@:param 数据库连接,存储过程名proname,
'''
#调用存储过程,传参数据库连接,存储过程名
def useMysqlPro(host,port,user,password,database,proname,inlist):
    conn = conMysql(host=host,port=port,user=user,password=password,database=database)
    cursor=conn.cursor()
    list=[]
    for inname in inlist:
        list.append(inname)
    try:
        cursor.callproc(proname,list)
        conn.commit()
        sql="select"
        for i in range(len(list)):
            sql+=" @_"+proname+"_"+str(i)+","
        cursor.execute(sql[:-1])
        resout = cursor.fetchall()
        return resout
    except Exception as e:
        return e
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    print(time.strftime("%Y%m%d%H%M%S",time.localtime()))
    li=['868','120109066870104324','2020-01-08','ces','','']
    resout=useMysqlPro('192.168.85.149',3306,'zl_longjiangbk','zl_longjiangbk','db_zl_longjiangbk','p_bzzb_jc',li)
    print(resout)
    time.sleep(2)
    resout1 = useMysqlPro('192.168.85.149', 3306, 'zl_longjiangbk', 'zl_longjiangbk', 'db_zl_longjiangbk', 'p_bzzb_sb',li)
    print(resout1)
    time.sleep(2)
    resout2 = useMysqlPro('192.168.85.149', 3306, 'zl_longjiangbk', 'zl_longjiangbk', 'db_zl_longjiangbk', 'p_bzzb_sbzs',li)
    print(resout2)
    time.sleep(2)
    resout3 = useMysqlPro('192.168.85.149', 3306, 'zl_longjiangbk', 'zl_longjiangbk', 'db_zl_longjiangbk', 'p_bzzb_cwbb',li)
    print(resout3)
    print(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    #pass
    # for i in range(10):
    #     print(i+1)
    #     sql="INSERT into djangochild_project (id,project_name,project_enname,project_desc,status) values ('%s','%s','%s','%s','%s')"%(str(i+100),"执行"+str(i+1),"晓得啥"+str(i+1),"信息的"+str(i+1),str(i+1))
    #     print(sql)
    #     updateMysql("localhost",3306,"zhangchuan","zhangchuan","dbtest",sql)
    # print(result)
    # inlist = []
    # outmap = {}
    # inlist.append("915301276787105486")
    # inlist.append("2020-04-13")
    # inlist.append("123")
    # inlist.append("None")
    # inlist.append("None")
    # resout=useMysqlPro("192.168.85.240",3306,"zl_pals","zl_pals","zl_pals","p_bzzb_jc",inlist)
    # print(resout[0])


