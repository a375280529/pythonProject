#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from pyclass import conOracle,forExcel
from forpub import forFinal
from forpub import geXingReport
import time
import traceback

#通用存储过程场景测试
class checkCallProNew(unittest.TestCase):
    #执行前调用
    def setUp(self):
        #新报告
        self.zbnum=0
        self.yonglinum=0
        self.chenggong=0
        self.shibai=0
        self.begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.zbmap = {}
        self.zbbiao = 0
        self.printtext=""
        self.errolist=[]
        #excel
        self.listallexcept = []
        self.listexcel=[]
        self.listcheck=[]
        self.resultcheck="true"
        self.ini=forFinal.getIni("loggerYuanMa.ini")
        self.url = self.ini["callpro"]["callproConnectUsername"]+"/"+self.ini["callpro"]["callproConnectPassword"]+"@"+ \
                   self.ini["callpro"]["callproConnectIp"]+"/"+self.ini["callpro"]["callproConnectTable"]
        self.list=forExcel.readExcelSheet(self.ini["callpro"]["callproexcelpath"])

    #执行后调用
    def tearDown(self):
        pass

    def test_call_pro(self):
        "存储过程场景测试"
        #循环获取第三个sheet的所有行数据
        try:
            for num in range(len(self.list[2])):
                # 新报告
                self.yonglinum+=1

                mapexcel={}
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
                    #新报告
                    self.shibai+=1

                    self.listcheck.append(maphave)
                    continue

                i=0
                inlist = []
                outmap = {}
                #获取和设置存储过程的入参和出参
                for all in range(int(innumber)):
                    i+=1
                    inlist.append(str(self.list[2][num]["value"+str(i)]))

                outmap["v_flag"] = "Float"
                outmap["v_remark"] = "String"
                tablelist=table.split(",")
                columnlist=column.split("&")
                wherelist=where.split(",")
                biaoshi="0"

                #调用存储过程
                result = conOracle.usePro(self.url, proname, inlist, outmap)
                #验证存储过程是否调用成功
                if result[int(innumber)] != 1.0:
                    pass
                else:
                    print("<p style='color:#9400D3'>数据编号" + str(num + 2)+"，纳税编号"+nsrsbh+"的存储过程执行异常！\n</p>")
                    self.printtext+="<p style='color:#9400D3'>数据编号" + str(num + 2)+"，纳税编号"+nsrsbh+"的存储过程执行异常！\n</p>\n"
                    continue
                #self.assertEqual(result[int(innumber)], 0.0)
                #self.assertEqual(result[int(innumber)+1], "成功")

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
                    col=columnlist[index].split(",")
                    t1=""
                    t2=""
                    ind=1
                    for co in col:
                        t1+="t.a"+str(ind)+" as "+co+","
                        t2+=co+" as a"+str(ind)+","
                        ind+=1
                    sql="select "+t1[:-1]+" from (select "+t2[:-1]+" from "+tablelist[index]+" "+allwhere+") t where rownum=1"
                    resultsql=conOracle.queryOracleReturnMap(self.url, sql)
                    if resultsql=={}:
                        maphave["数据编号" + str(num + 2)+"，纳税编号"+nsrsbh+"的"+tablelist[index]+"表"] = "未查询到任何数据，请检查传入sql，传入sql为"+sql
                        self.resultcheck = "false"
                        # 新报告
                        self.shibai += 1

                        self.listcheck.append(maphave)
                        sqlbiaoshi = "1"
                        maphave={}
                    checklist.append(resultsql)

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
                                    mapzc={}
                                    mapzc["指标名"]=name
                                    mapzc["期望值"]=exceptmap[name]
                                    mapzc["实际值"]=str(check[name])
                                    if exceptmap[name]=="":
                                        exceptmap[name]="None"
                                    if exceptmap[name]=="notNone":
                                        if str(check[name]) == "None":
                                            self.resultcheck = "false"
                                            self.listallexcept.append(name)
                                            listhave.append(name + ",期望值：" + exceptmap[name] + ",实际值：" + str(check[name]))
                                            mapzc["red"] = "true"
                                            biaoshi = "1"
                                            #新报告
                                            zbhaskey=self.zbmap.get(name)
                                            if zbhaskey!=None:
                                                zbvalue=self.zbmap.pop(name)
                                                errornum=zbvalue.pop("zhibiaoerror")
                                                zbvalue["zhibiaoerror"]=errornum+1
                                                self.zbmap.setdefault(name,zbvalue)
                                                self.zbbiao = 1
                                            else:
                                                self.zbmap.setdefault(name, {"zhibiaopass":0,"zhibiaoerror":1})
                                                self.zbbiao = 1

                                        else:
                                            mapzc["red"] = "false"
                                            # 新报告
                                            zbhaskey = self.zbmap.get(name)
                                            if zbhaskey != None:
                                                zbvalue = self.zbmap.pop(name)
                                                passnum = zbvalue.pop("zhibiaopass")
                                                zbvalue["zhibiaopass"] = passnum + 1
                                                self.zbmap.setdefault(name, zbvalue)
                                            else:
                                                self.zbmap.setdefault(name, {"zhibiaopass": 1, "zhibiaoerror": 0})

                                        excelishave = "1"
                                    else:
                                        if str(check[name]) != exceptmap[name] and str(check[name])+".0" != exceptmap[name] and str(check[name]) != exceptmap[name]+".0":
                                            self.resultcheck = "false"
                                            self.listallexcept.append(name)
                                            listhave.append(name+",期望值："+exceptmap[name]+",实际值："+str(check[name]))
                                            mapzc["red"] = "true"
                                            biaoshi = "1"
                                            # 新报告
                                            zbhaskey = self.zbmap.get(name)
                                            if zbhaskey != None:
                                                zbvalue = self.zbmap.pop(name)
                                                errornum = zbvalue.pop("zhibiaoerror")
                                                zbvalue["zhibiaoerror"] = errornum + 1
                                                self.zbmap.setdefault(name, zbvalue)
                                                self.zbbiao = 1
                                            else:
                                                self.zbmap.setdefault(name, {"zhibiaopass": 0, "zhibiaoerror": 1})
                                                self.zbbiao = 1
                                        else:
                                            mapzc["red"] = "false"
                                            # 新报告
                                            zbhaskey = self.zbmap.get(name)
                                            if zbhaskey != None:
                                                zbvalue = self.zbmap.pop(name)
                                                passnum = zbvalue.pop("zhibiaopass")
                                                zbvalue["zhibiaopass"] = passnum + 1
                                                self.zbmap.setdefault(name, zbvalue)
                                            else:
                                                self.zbmap.setdefault(name, {"zhibiaopass": 1, "zhibiaoerror": 0})
                                        excelishave="1"
                        if excelishave=="0":
                            self.resultcheck = "false"
                            self.listallexcept.append(name)
                            listhave.append(name + ",该字段在excel中的column中未添加，导致该字段未做验证，请添加后重新执行")
                            biaoshi = "1"
                        #excel
                        listzc.append(mapzc)
                    if biaoshi == "1":
                        maphave["数据编号"+str(num+2)+"，纳税编号"+nsrsbh]=listhave
                        self.listcheck.append(maphave)
                        # 新报告
                        self.shibai += 1
                    else:
                        # 新报告
                        self.chenggong += 1
                    #excel
                    mapexcel["纳税编号"+nsrsbh+"，数据编号"+str(num+2)]=listzc
                    self.listexcel.append(mapexcel)
                except Exception as e:
                    self.printtext +=str(e)+"\n"
                    print(e)
                    self.resultcheck = "false"
        except:
            erro = traceback.format_exc()
            self.errolist.append(erro)
            self.resultcheck = "false"
        #excel
        try:
            forExcel.getExcelColor(self.listexcel)
        except:
            excelerro = traceback.format_exc()
            self.errolist.append(excelerro)
            self.resultcheck = "false"
        #打印出用例执行结果信息
        if self.resultcheck=="true":
            print("<p style='color:green'>测试用例执行成功!</p>")
            self.printtext +="<p style='color:green'>测试用例执行成功!</p>\n"
        else:
            print("<p style='color:red'>测试用例执行失败!</p><p style='color:red'>失败数据详情：</p>")
            self.printtext +="<p style='color:red'>测试用例执行失败!</p><p style='color:red'>失败数据详情：</p>\n"
        for val in self.listcheck:
            print("<p style='color:red'>",val,"</p>")
            self.printtext +="<p style='color:red'>"+str(val)+"</p>\n"
        if self.listallexcept!=[]:
            print("<p style='color:red'>所有异常指标集合：",set(self.listallexcept),"</p>")
            self.printtext +="<p style='color:red'>所有异常指标集合："+str(set(self.listallexcept))+"</p>"

        self.errolist.append(self.printtext)
        # 新报告
        end_time = int(time.time())
        start_time = int(time.mktime(time.strptime(self.begin_time, '%Y-%m-%d %H:%M:%S')))
        alltime = str(end_time - start_time) + 's'
        testResult=self.errolist
        if self.resultcheck == "true":
            resultmap={'description': '存储过程场景测试', 'spendTime': alltime, 'status': '成功','log':testResult}
        else:
            resultmap = {'description': '存储过程场景测试', 'spendTime': alltime, 'status': '失败','log':testResult}
        if self.zbbiao!=1:
            fimap = {"testPass": self.chenggong, "testName": "模型规则用例", "testAll": self.yonglinum,"testFail": self.shibai,"beginTime": self.begin_time, "totalTime": alltime,  "testzhibiao": "null","testResult":[resultmap]}
        else:
            #去除成功的数据
            for zbk in list(self.zbmap.keys()):
                if self.zbmap[zbk]["zhibiaoerror"]==0:
                    del self.zbmap[zbk]
                    continue
            fimap = {"testPass": self.chenggong, "testName": "模型规则用例", "testAll": self.yonglinum,"testFail": self.shibai, "beginTime": self.begin_time, "totalTime": alltime, "testzhibiao": self.zbmap,"testResult":[resultmap]}
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        geXingReport.report(filename="自动化测试报告" + now, description="自动化测试报告用例", log_path="E:\\test\\baogao",fimap=fimap)
        self.assertEqual("true",self.resultcheck)

if __name__ == '__main__':
    unittest.main()