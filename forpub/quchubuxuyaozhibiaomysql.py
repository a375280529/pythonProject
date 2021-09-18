# -*-coding:utf-8-*-
import time

from pyclass import forExcel as fe
import forFinal
from pyclass import conMysql

#用于其他银行标准指标跟source库标准指标比对，拿出所需要的指标，去除不需要的指标
if __name__ == '__main__':
    ini = forFinal.getIni("loggerMysql.ini")
    host = ini["callpro"]["callproConnectIp"]
    port = ini["callpro"]["callproConnectPort"]
    user = ini["callpro"]["callproConnectUsername"]
    password = ini["callpro"]["callproConnectPassword"]
    database = ini["callpro"]["callproConnectTable"]
    #url = ini["callpro"]["callproConnectUsername"] + "/" + ini["callpro"]["callproConnectPassword"] + "@" + ini["callpro"]["callproConnectIp"] + "/" + ini["callpro"]["callproConnectTable"]
    list=fe.readExcelSheet("F:\\pingan\\平安风控.xlsx")
    listone = []
    listtwo = []
    listall=list[1]
    listkey=list[1][0].keys()
    sql = "select * from T_GSSF_ZB_HSJ limit 1"
    re = conMysql.queryMysqlReturnMap(host,port,user,password,database, sql)
    key = re.keys()
    listka=[]
    for lk in listkey:
        for keyva in key:
            if lk==str(keyva).upper():
                listka.append(lk)
    listva=[]
    for cl in listall:
        mapva={}
        for clkey in cl.keys():
            for ka in listka:
                if clkey==ka:
                    if clkey=="NSRSBH" or clkey=="LRSJ":
                        mapva[clkey]=cl[clkey]
                    else:
                        mapva[clkey] = clkey+"="+cl[clkey]
        listva.append(mapva)
    map={}
    list=[]
    map["shee1"] = listva
    list.append(map)
    fe.getExcel(list)

