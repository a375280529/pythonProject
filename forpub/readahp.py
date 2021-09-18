#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyclass import forExcel
import cx_Oracle as cx
import time

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

if __name__ == '__main__':
    print("执行中。。。")
    values=forExcel.readExcelSheet("F:\\ahp\\ahp中行.xlsx")
    firstval=values[0][0]
    guize=firstval["jisuangz"]
    calname=firstval["calname"]
    intval=firstval["intval"]
    outval=firstval["outval"]
    nsrsbh = firstval["nsrsbh"]
    initvalscore = firstval["initvalscore"]
    checktrue = firstval["checktrue"]
    checkkey=checktrue.split("&")[0]
    checkva=checktrue.split("&")[1]
    checkvalue = firstval["checkvalue"]
    mapnull={}
    mapyuanshi={}
    for init in initvalscore.split(","):
        listnull=init.split("&")
        mapnull[listnull[0]]=listnull[2]+"&"+listnull[3]+"&"+listnull[4]
        mapyuanshi[listnull[0]] =listnull[1]
    mapname={}
    for all in values[0]:
        listname=[]
        if all["coulmnname"] in mapname:
            listname=mapname[all["coulmnname"]]
            listname.append(all)
            mapname[all["coulmnname"]]=listname
        else:
            listname.append(all)
            mapname[all["coulmnname"]]=listname
    biaoshi=""
    sgtable=""
    for coulmnkeys in mapname.keys():
        if biaoshi!="" and biaoshi!=mapname[coulmnkeys][0]["coulmnname"]:
            print(sgtable,biaoshi,mapyuanshi[biaoshi],nsrsbh)
            sqla="update %s set %s='%s' where nsrsbh='%s'" %(sgtable,biaoshi,mapyuanshi[biaoshi],nsrsbh)
            updateOracle("szzh_test/szzh_test@192.168.85.81:1521/emserver", sqla)
        biaoshi=mapname[coulmnkeys][0]["coulmnname"]
        sgtable=mapname[coulmnkeys][0]["tablename"]
        for quanzhi in mapname[coulmnkeys]:
            value=""
            if quanzhi["value"]=="None":
                value=''
            else:
                value = quanzhi["value"]
            sql="update %s set %s='%s' where nsrsbh='%s'" %(quanzhi["tablename"],quanzhi["coulmnname"],value,nsrsbh)
            updateOracle("szzh_test/szzh_test@192.168.85.81:1521/emserver", sql)
            inlist = []
            outmap = {}
            for inli in intval.split("&"):
                inlist.append(str(inli))
            for outl in outval.split("&"):
                outdou=outl.split(",")
                outmap[outdou[0]] = outdou[1]
            result=usePro("szzh_test/szzh_test@192.168.85.81:1521/emserver", calname, inlist, outmap)
            if str(result[int(float(checkkey))-1])==str(checkva) or str(result[int(float(checkkey))-1])==str(checkva+".0"):
                endscore=result[int(float(checkvalue))-1]
                totalscore=0.0
                for mapscorekey in mapnull.keys():
                    if mapscorekey==quanzhi["coulmnname"]:
                        pass
                    else:
                        zz=mapnull[mapscorekey].split("&")
                        totalscore+=float(zz[0])*float(zz[1])*float(zz[2])
                totalscore+=float(quanzhi["score"])*float(quanzhi["yscqz"])*float(quanzhi["zzcqz"])
                rpguize=guize.replace("Score",str(totalscore))
                ts=eval(rpguize)
                ts = ('%.4f' % ts)
                ts=quzero(ts)
                if ts=="-0" or ts=="0":
                    ts="0.0"
                if ts==str(result[int(float(checkvalue))-1]):
                    pass
                else:
                    print(quanzhi["coulmnname"]+"指标区间取值为"+quanzhi["value"]+"时发生异常！")
                    print("期望值："+ts,"实际值:"+str(result[int(float(checkvalue))-1]))
            else:
                print("存储过程异常！")
    print("执行完成。。。")

