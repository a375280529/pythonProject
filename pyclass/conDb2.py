#!/usr/bin/python
# -*- coding: utf-8 -*-

import ibm_db_dbi as db
import ibm_db
import logging

def conDb(host='',port='',user='',password='',database=''):
    # 连接数据库
    conn = db.connect("PORT="+port+";PROTOCOL=TCPIP;AUTHENTICATION=SERVER;",host=host,database=database,user=user,password=password)
    return conn

#查询多条数据返回所有数据值的List
def queryDb(host,port,user,password,database, sql):
    conn = conDb(host=host,port=port,user=user,password=password,database=database)
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
def queryDbReturnMap(host,port,user,password,database, sql):
    conn = conDb(host=host,port=port,user=user,password=password,database=database)
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
def queryDbAllReturnList(host,port,user,password,database, sql):
    conn = conDb(host=host,port=port,user=user,password=password,database=database)
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


def updateDb(host,port,user,password,database, sql):
    # 连接数据库
    conn = conDb(host=host,port=port,user=user,password=password,database=database)
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
def useDbPro(host,port,user,password,database,proname,inlist):
    cont = "DATABASE=" + database + ";HOSTNAME=" + host + ";PORT=" + port + ";PROTOCOL=TCPIP;UID=" + user + ";PWD=" + password+";AUTHENTICATION=SERVER;"
    conn = ibm_db.connect(cont, "","")
    biaoshi=0
    try:
        sql = 'CALL '
        sql+=proname+"("
        for li in inlist:
            if li=="?" or li=="？":
                biaoshi+=1
                sql+="?,"
            else:
                sql+="'"+li+"',"
        sql=sql[:-1]+")"
        stmt = ibm_db.prepare(conn, sql)

        for i in range(biaoshi):
            ibm_db.bind_param(stmt,i+1,'',ibm_db.SQL_PARAM_OUTPUT)
        resout = ibm_db.execute(stmt)
        return resout
    except Exception as e:
        return e
    finally:
        conn.close()

if __name__ == '__main__':
    #pass
    # inlist=["yyds","666","?"]
    # ff=useDbPro('192.168.85.231','50000','db2inst1','db2inst1','test',"DEMO1201",inlist)
    # print(ff)
    sql="select * from zx_nsrjcxx"
    df=queryDbReturnMap('192.168.85.231','50000','db2inst1','db2inst1','test', sql)
    print(df)