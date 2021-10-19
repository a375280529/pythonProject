#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import unittest
from pyclass import conOracle,forExcel
from forpub import forFinal
import logging

#通用模型规则场景测试
class checkCallProForRules(unittest.TestCase):
    #执行前调用
    def setUp(self):
        self.listcheck=[]
        self.resultcheck="true"
        self.ini=forFinal.getIni("loggerRules.ini")
        self.url = self.ini["callpro"]["callproConnectUsername"]+"/"+self.ini["callpro"]["callproConnectPassword"]+"@"+ \
                   self.ini["callpro"]["callproConnectIp"]+"/"+self.ini["callpro"]["callproConnectTable"]
        self.list=forExcel.readExcelSheet(self.ini["callpro"]["callproexcelpath"])

    #执行后调用
    def tearDown(self):
        pass

    def test_call_pro(self):
        "模型规则场景测试"
        #循环获取第二个sheet的所有行数据
        for num in range(len(self.list[1])):
            maphave={}
            findrulebiaoshi="0"
            rulenum=self.list[1][num]['rulenum']
            updatecolumn = self.list[1][num]['updatecolumn']
            updatevalue = self.list[1][num]['updatevalue']
            exceptvalue = self.list[1][num]['exceptvalue']

            proname = ""
            updatetable=""
            updatewhere = ""
            proreturnvalue = ""
            innumber = ""
            checkvalue = ""
            checktable = ""
            checkcolumn = ""
            checkwhere = ""

            #用第二个sheet的rulenum去获取第一个sheet的规则信息
            for n in range(len(self.list[0])):
                if rulenum==self.list[0][n]['rulenum']:
                    proname = self.list[0][n]['sp']
                    updatetable = self.list[0][n]['updatetable']
                    updatewhere = self.list[0][n]['updatewhere']
                    proreturnvalue = self.list[0][n]['proreturnvalue']
                    innumber = self.list[0][n]['innumber']
                    checkvalue = self.list[0][n]['checkvalue']
                    checktable = self.list[0][n]['checktable']
                    checkcolumn = self.list[0][n]['checkcolumn']
                    checkwhere = self.list[0][n]['checkwhere']
                    findrulebiaoshi="1"
            #判断第二个sheet数据是否在第一个sheet有对应规则
            if findrulebiaoshi=="0":
                maphave["数据编号" + str(num + 2)] = "未匹配到sheet1中对应的规则信息"
                self.resultcheck = "false"
                self.listcheck.append(maphave)
                continue

            i=0
            inlist = []
            outmap = {}
            #获取和设置存储过程的入参和出参
            for all in range(int(innumber)):
                i+=1
                inlist.append(str(self.list[1][num]["value"+str(i)]))

            omap=proreturnvalue
            olist=omap.split("&")
            for ova in olist:
                outm=ova.split(",")
                outmap[outm[0]] = outm[1]

            updatetablelist=updatetable.split("&")
            updatewherelist=updatewhere.split("&")
            #分割后还需英文逗号分割
            updatecolumnlist=updatecolumn.split("&")
            updatevaluelist=updatevalue.split("&")

            huanyuansqllist=[]
            isoksqllist=[]
            #获取历史还原数据用于还原数据和更改历史数据用于验证规则
            for ut in range(len(updatetablelist)):
                utable=updatetablelist[ut]
                ucolumnlist=updatecolumnlist[ut].split(",")
                uvaluelist = updatevaluelist[ut].split(",")
                uwhere=updatewherelist[ut]
                wheres = uwhere.split("'")
                allwhere = ""
                for ss in wheres:
                    if ss.isdigit():
                        allwhere += "'" + self.list[1][num]["value" + ss] + "'"
                    else:
                        allwhere += ss
                #记录原始数据的sql
                yuanshisql="select "
                #更改表数据的sql
                upsql="update "+utable+" set "
                for ucolumn in range(len(ucolumnlist)):
                    yuanshisql+="t."+ucolumnlist[ucolumn].strip("\n")+","
                    upsql+=ucolumnlist[ucolumn].strip("\n")+"="+uvaluelist[ucolumn].strip("\n")+","
                upsql=upsql[:-1]+" "+allwhere
                yuanshisql=yuanshisql[:-1]+" from (select * from "+utable+" "+allwhere+"order by lrsj desc) t where rownum=1"
                yuanshimap=conOracle.queryOracleReturnMap(self.url,yuanshisql)
                allysql="update "
                yuansql=""
                for keys in yuanshimap.keys():
                    try:
                        if yuanshimap[keys]==None:
                            yuansql+=keys+"=null,"
                        else:
                            yuansql += keys + "='" + yuanshimap[keys] + "',"
                    except:
                        if yuanshimap[keys] == None:
                            yuansql += keys + "=null,"
                        else:
                            yuansql += keys + "=" + str(yuanshimap[keys]) + ","
                allysql+=utable+" set "+yuansql[:-1]+" "+allwhere
                huanyuansqllist.append(allysql)
                conOracle.updateOracle(self.url,upsql)
                time.sleep(1)

            #调用存储过程
            result = conOracle.usePro(self.url, proname, inlist, outmap)

            #验证存储过程是否调用成功
            if result[int(checkvalue)-1] != 1.0:
                pass
            else:
                print("<p style='color:#9400D3'>数据编号" + str(num + 2)+"，存储过程执行异常！\n</p>")
                continue

            cwheres = checkwhere.split("'")
            allcheckwhere = ""
            for fs in cwheres:
                if fs.isdigit():
                    allcheckwhere += "'" + self.list[1][num]["value" + fs] + "'"
                else:
                    allcheckwhere += fs

            #获取校验信息
            checksql="select t."+checkcolumn+" from (select * from "+checktable+" "+allcheckwhere+") t where rownum=1"
            checkmap = conOracle.queryOracleReturnMap(self.url, checksql)
            endresult=checkmap[checkcolumn.upper()]
            exceptvaluelist=exceptvalue.split(";")
            biaoshi="0"
            exceptrule=""
            for exceptva in exceptvaluelist:
                if exceptva in endresult:
                    pass
                else:
                    biaoshi="1"
                    exceptrule+=exceptva+";"
                    self.resultcheck = "false"
            if biaoshi=="1":
                maphave["数据编号" + str(num + 2)] = exceptrule+"的期望命中规则结果未命中"
                self.listcheck.append(maphave)

            # 执行数据的还原
            for hysql in range(len(huanyuansqllist)):
                conOracle.updateOracle(self.url, huanyuansqllist[hysql])

            time.sleep(1)

        #打印出用例执行结果信息
        if self.resultcheck=="true":
            print("<p style='color:green'>测试用例执行成功!</p>")
        else:
            print("<p style='color:red'>测试用例执行失败!</p><p style='color:red'>失败数据详情：</p>")
        for val in self.listcheck:
            print("<p style='color:red'>",val,"</p>")
        self.assertEqual("true",self.resultcheck)

if __name__ == '__main__':
    unittest.main()