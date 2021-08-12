# -*-coding:utf-8-*-
import time

from pyclass import forExcel as fe
import forFinal
from pyclass import conOracle

#用于其他银行标准指标跟source库标准指标比对，拿出所需要的指标，去除不需要的指标
if __name__ == '__main__':
    isrulenum="c1"
    list1=[]
    list2=[]
    map1={}
    map2={}
    ini = forFinal.getIni("logger.ini")
    url = ini["callpro"]["callproConnectUsername"] + "/" + ini["callpro"]["callproConnectPassword"] + "@" + ini["callpro"]["callproConnectIp"] + "/" + ini["callpro"]["callproConnectTable"]
    list=fe.readExcelSheet("F:\\asd\\1.xlsx")
    listone = []
    listtwo = []
    for num in range(len(list[2])):
        nsrsbh = list[2][num]['nsrsbh']
        rulenum = list[2][num]['rulenum']
        if rulenum == isrulenum:
            pass
        else:
            continue
        innumber = list[2][num]['innumber']
        outnumber = list[2][num]['outnumber']
        # 用第三个sheet的rulenum去获取第二个sheet的规则信息
        for n in range(len(list[1])):
            if rulenum == list[1][n]['rulenum']:
                table = list[1][n]['table']

        sql ="select t.* from (select * from "+table+") t where rownum=1"
        re=conOracle.queryOracleReturnMap(url, sql)
        key=re.keys()
        i=int(innumber)
        listhave = []
        maphave = {}
        mapsame = {}
        mapnotsame= {}
        for number in range(int(outnumber)):
            i += 1
            forlist = str(list[2][num]["value" + str(i)]).split("=")
            maphave[forlist[0]] = forlist[1]

        b=0
        c=0
        keyname=""
        for k in key:
            biaoshi=0
            mapvalue=""
            for ma in maphave.keys():
                if k==ma:
                    biaoshi=1
                    mapvalue=ma+"="+maphave[ma]
            if biaoshi==1:
                b += 1
                mapsame["value"+str(b)]=mapvalue
                keyname+=","+k
            else:
                c+=1
                mapnotsame["value" + str(c)]=k
        listone.append(mapsame)
        listtwo.append(mapnotsame)
        print(keyname[1:])
    map1["shee1"]=listone
    list1.append(map1)
    map2["shee1"] = listtwo
    list2.append(map2)
    print(list1)
    print(list2)
    fe.getExcel(list1)
    time.sleep(2)
    fe.getExcel(list2)

