#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from pyclass import conDb2,forExcel
from forpub import forFinal

#通用存储过程场景测试
class checkCallProNew(unittest.TestCase):
    #执行前调用
    def setUp(self):
        #excel
        self.listexcel=[]
        self.listcheck=[]
        self.resultcheck="true"
        self.ini=forFinal.getIni("loggerDb.ini")
        self.host=self.ini["callpro"]["callproConnectIp"]
        self.port=self.ini["callpro"]["callproConnectPort"]
        self.name = self.ini["callpro"]["callproConnectUsername"]
        self.password = self.ini["callpro"]["callproConnectPassword"]
        self.table = self.ini["callpro"]["callproConnectTable"]
        self.list=forExcel.readExcelSheet(self.ini["callpro"]["callproexcelpath"])

    #执行后调用
    def tearDown(self):
        pass

    def test_call_pro(self):
        "存储过程场景测试"
        #循环获取第三个sheet的所有行数据
        for num in range(len(self.list[2])):
            mapexcel = {}
            listhave=[]
            maphave={}
            findrulebiaoshi="0"
            nsrsbh = self.list[2][num]['nsrsbh']
            rulenum=self.list[2][num]['rulenum']
            innumber = self.list[2][num]['innumber']
            outnumber = self.list[2][num]['outnumber']
            proname=""
            table = ""
            column = ""
            where = ""

            #用第三个sheet的rulenum去获取第二个sheet的规则信息
            for n in range(len(self.list[1])):
                if rulenum==self.list[1][n]['rulenum']:
                    proname = self.list[1][n]['sp']
                    table = self.list[1][n]['table']
                    column = self.list[1][n]['column']
                    where = self.list[1][n]['where']
                    findrulebiaoshi="1"
            #判断第三个sheet数据是否在第二个sheet有对应规则
            if findrulebiaoshi=="0":
                maphave["数据编号" + str(num + 2)+"，纳税编号"+nsrsbh] = "未匹配到对应的规则信息"
                self.resultcheck = "false"
                self.listcheck.append(maphave)
                continue

            i=0
            inlist = []
            #获取和设置存储过程的入参和出参
            for all in range(int(innumber)):
                i+=1
                inlist.append(str(self.list[2][num]["value"+str(i)]))

            tablelist=table.split(",")
            columnlist=column.split("&")
            wherelist=where.split(",")
            biaoshi="0"

            #调用存储过程
            conDb2.useDbPro(self.host,self.port,self.name,self.password,self.table, proname, inlist)

            sqlbiaoshi="0"
            checklist=[]
            #循环获取需验证的表的信息
            for index in range(len(tablelist)):
                wheres=wherelist[index].split("'")
                allwhere=""
                for ss in wheres:
                    if ss.isdigit():
                        allwhere+="'"+self.list[2][num]["value"+ss]+"'"
                    else:
                        allwhere+=ss
                sql="select "+columnlist[index]+" from "+tablelist[index]+" "+allwhere
                resultsql=conDb2.queryDbAllReturnList(self.host,self.port,self.name,self.password,self.table, sql)
                if len(resultsql)==0:
                    maphave["数据编号" + str(num + 2)+"，纳税编号"+nsrsbh+"的"+tablelist[index]+"表"] = "结果表中未查询到任何数据，存储过程执行异常"
                    self.resultcheck = "false"
                    self.listcheck.append(maphave)
                    sqlbiaoshi = "1"
                    maphave={}
                    continue
                mapre = {}
                for resultva in resultsql:
                    mapre[resultva["INDEX_CODE"].upper()] = resultva["INDEX_VALUE"]
                checklist.append(mapre)

            if sqlbiaoshi=="1":
                continue

            exceptmap={}
            #获取excel中需验证的数据值
            for number in range(int(outnumber)):
                i+=1
                forlist=str(self.list[2][num]["value"+str(i)]).split("=")
                exceptmap[forlist[0]]=forlist[1]
            #excel
            listzc=[]
            try:
                #验证实际值与期望值是否一致
                for name in exceptmap.keys():
                    excelishave="0"
                    for check in checklist:
                        for checkname in check.keys():
                            if name == checkname:
                                #excel
                                mapzc = {}
                                mapzc["指标名"]=name
                                mapzc["期望值"]=exceptmap[name]
                                mapzc["实际值"]=str(check[name])

                                if exceptmap[name]=="":
                                    exceptmap[name]="None"
                                if exceptmap[name]=="notNone":
                                    if str(check[name]) == "None":
                                        self.resultcheck = "false"
                                        listhave.append(name + ",期望值：" +exceptmap[name]+ ",实际值：" + str(check[name]))
                                        biaoshi = "1"
                                    excelishave = "1"
                                else:
                                    if str(check[name]).strip() != exceptmap[name] and str(check[name]).strip()+".0" != exceptmap[name] and str(check[name]).strip() != exceptmap[name]+".0" and str(check[name]).strip() != exceptmap[name]+"000":
                                        self.resultcheck = "false"
                                        listhave.append(name+",期望值："+exceptmap[name]+",实际值："+str(check[name]))
                                        biaoshi = "1"
                                    excelishave="1"
                    if excelishave=="0":
                        self.resultcheck = "false"
                        listhave.append(name + ",该字段在excel中的column中未添加，导致该字段未做验证，请添加后重新执行")
                        biaoshi = "1"
                    #excel
                    listzc.append(mapzc)

                if biaoshi == "1":
                    maphave["数据编号"+str(num+2)+"，纳税编号"+nsrsbh]=listhave
                    self.listcheck.append(maphave)
                #excel
                mapexcel["纳税编号"+nsrsbh]=listzc
                self.listexcel.append(mapexcel)
            except Exception as e:
                print(e)
        #excel
        forExcel.getExcel(self.listexcel)
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