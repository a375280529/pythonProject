#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from pyclass import conOracle,forExcel
from forpub import forFinal

#通用存储过程场景测试
class checkCallPro(unittest.TestCase):
    #执行前调用
    def setUp(self):
        self.listcheck=[]
        self.resultcheck="true"
        self.ini=forFinal.getIni("logger.ini")
        self.url = self.ini["callpro"]["callproConnectUsername"]+"/"+self.ini["callpro"]["callproConnectPassword"]+"@"+\
                   self.ini["callpro"]["callproConnectIp"]+"/"+self.ini["callpro"]["callproConnectTable"]
        self.list=forExcel.readExcel(self.ini["callpro"]["callproexcelpath"])

    #执行后调用
    def tearDown(self):
        pass

    def test_p_bzzb_js_lfyh(self):
        "p_bzzb_js_lfyh存储过程场景测试"
        for num in range(len(self.list)):
            proname = self.list[num]['sp']
            table=self.list[num]['table']
            column=self.list[num]['column']
            where =self.list[num]['where']
            nsrsbh = self.list[num]['nsrsbh']
            innumber = self.list[num]['innumber']
            outnumber = self.list[num]['outnumber']
            i=0
            inlist = []
            outmap = {}
            for all in range(int(innumber)):
                i+=1
                inlist.append(str(self.list[num]["value"+str(i)]))
            outmap["v_flag"] = "number"
            outmap["v_remark"] = "str"
            tablelist=table.split(",")
            columnlist=column.split("&")
            wherelist=where.split(",")
            biaoshi="0"
            maphave={}
            listhave=[]

            result = conOracle.usePro(self.url, proname, inlist, outmap)

            if result[int(innumber)] == 0.0 and result[int(innumber)+1] == "成功":
                pass
            else:
                print("<p>第"+str(num+1)+"次存储过程执行异常！\n</p>")
            self.assertEqual(result[int(innumber)], 0.0)
            self.assertEqual(result[int(innumber)+1], "成功")

            checklist=[]
            for index in range(len(tablelist)):
                sql="select t.* from (select "+columnlist[index]+" from "+tablelist[index]+" "+wherelist[index]+" order by lrsj desc) t where rownum=1"
                resultsql=conOracle.queryOracleReturnMap(self.url, sql)
                checklist.append(resultsql)

            exceptmap={}
            for number in range(int(outnumber)):
                i+=1
                forlist=str(self.list[num]["value"+str(i)]).split("=")
                exceptmap[forlist[0]]=forlist[1]


            try:
                for name in exceptmap.keys():
                    excelishave="0"
                    for check in checklist:
                        for checkname in check.keys():
                            if name == checkname:
                                if exceptmap[name]=="":
                                    exceptmap[name]="None"
                                if str(check[name]) != exceptmap[name]:
                                    self.resultcheck = "false"
                                    listhave.append(name+",期望值："+exceptmap[name]+",实际值："+str(check[name]))
                                    biaoshi = "1"
                                excelishave="1"
                    if excelishave=="0":
                        self.resultcheck = "false"
                        listhave.append(name + ",该字段在excel中的column中未添加，导致该字段未做验证，请添加后重新执行")
                        biaoshi = "1"

                if biaoshi == "1":
                    maphave["数据编号"+str(num+2)+"，税号："+nsrsbh]=listhave
                    self.listcheck.append(maphave)
            except Exception as e:
                print(e)
        if self.resultcheck=="true":
            print("<p style='color:green'>测试用例执行成功!</p>")
        else:
            print("<p style='color:red'>测试用例执行失败!</p><p style='color:red'>失败数据详情：</p>")
        for val in self.listcheck:
            print("<p style='color:red'>",val,"</p>")
        self.assertEqual("true",self.resultcheck)

if __name__ == '__main__':
    unittest.main()


