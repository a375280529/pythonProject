# -*-coding:utf-8-*-
import time

from pyclass import forExcel as fe
import forFinal
from pyclass import conMysql

#用于其他银行标准指标跟source库标准指标比对，拿出所需要的指标，去除不需要的指标
if __name__ == '__main__':
    isrulenum = "c6"
    ini = forFinal.getIni("loggerMysql.ini")
    host = ini["callpro"]["callproConnectIp"]
    port = ini["callpro"]["callproConnectPort"]
    user = ini["callpro"]["callproConnectUsername"]
    password = ini["callpro"]["callproConnectPassword"]
    database = ini["callpro"]["callproConnectTable"]
    print(host)
    print(port)
    print(user)
    print(password)
    print(database)
    #url = ini["callpro"]["callproConnectUsername"] + "/" + ini["callpro"]["callproConnectPassword"] + "@" + ini["callpro"]["callproConnectIp"] + "/" + ini["callpro"]["callproConnectTable"]
    list=fe.readExcelSheet("F:\\asd\\51ku\\newgozcfzxx.xlsx")
    listone = []
    listtwo = []
    listall=list[2]

    table=""
    for n in range(len(list[1])):
        if isrulenum == list[1][n]['rulenum']:
            table = list[1][n]['table']
            break
    #print(listall)
    #print(len(listall))
    sql = "select * from %s limit 1"%(table)
    print(sql)
    re = conMysql.queryMysqlReturnMap(host,port,user,password,database, sql)
    key = re.keys()
    listka=[]
    listnohave=[]
    for cl in listall:
        c=0
        b=0
        keyname=""
        if cl["rulenum"]!=isrulenum:
            continue
        mapva={}
        mapnohave={}
        for ka in key:
            biaoshi=0
            for clkey in cl.keys():
                if cl[clkey].split("=")[0]==str(ka).upper():
                    b+=1
                    biaoshi=1
                    mapva["value" + str(b)]=cl[clkey]
            if biaoshi==1:
                keyname+=","+ka
            else:
                c+=1
                mapnohave["value" + str(c)]=ka
        listka.append(mapva)
        listnohave.append(mapnohave)
        print(keyname[1:].upper())
    #print(listka)
    #print(listnohave)
    mapa={}
    mapb={}
    lista=[]
    listb=[]
    mapa["shee1"] = listka
    lista.append(mapa)
    mapb["shee1"] = listnohave
    listb.append(mapb)
    fe.getExcel(lista)
    time.sleep(2)
    fe.getExcel(listb)

