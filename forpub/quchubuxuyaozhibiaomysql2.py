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
    list=fe.readExcelSheet("F:\\asd\\abc.xlsx")
    listone = []
    listtwo = []
    listall=list[2]
    print(len(listall))
    sql = "select * from t_jc_zb limit 1"
    re = conMysql.queryMysqlReturnMap(host,port,user,password,database, sql)
    key = re.keys()
    listka=[]
    for cl in listall:
        mapva={}
        for clkey in cl.keys():
            for ka in key:
                if cl[clkey].split("=")[0]==str(ka).upper():
                    mapva[clkey]=cl[clkey]
        listka.append(mapva)
    print(listka)
    map={}
    list=[]
    map["shee1"] = listka
    list.append(map)
    fe.getExcel(list)

