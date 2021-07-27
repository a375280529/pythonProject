#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import finalClass as fc


if __name__ == '__main__':
    exepath = os.path.realpath(sys.executable)
    endpath = exepath.split(exepath.split("\\")[-1])[0]
    exclepath=os.path.join(os.path.abspath('.'), endpath + "juece.xlsx")
    print(endpath)
    ff=fc.readExcelRealGeShi("D:\\juece\\juece.xlsx")
    for hh in ff:
        params=hh
        headers={}
        dd=fc.getJsonForPostInterface("http://192.168.86.114:9080/api/v1/engine/execute/decision?tenantId=anti_fraud_test&deploymentId=16560&collectRulesInfo=true&collectVariables=true&collectIndicatorInfo=true&collectVariables=true",params,headers)
        print(dd)


# # 通用存储过程场景测试
# class checkCallProNew(unittest.TestCase):
#     # 执行前调用
#     def setUp(self):
#         self.resultcheck = "true"
#         self.ini = fc.getIni("logger.ini")
#         exepath = os.path.realpath(sys.executable)
#         endpath = exepath.split(exepath.split("\\")[-1])[0]
#         excelpath = os.path.join(os.path.abspath('.'), endpath + self.ini["callpro"]["callproexcelpath"])
#         self.list = fc.readExcelRealGeShi(excelpath)
#
#     # 执行后调用
#     def tearDown(self):
#         pass
#
#     def test_call_pro(self):
#         "决策引擎测试"
#
#         # 获取excel所有行数据
#         for num in range(len(self.list)):
#             mapexcel = {}
#             listhave = []
#             maphave = {}
#             findrulebiaoshi = "0"
#             # nsrsbh = "异常时显示的醒目标识名"
#             rulenum = self.list[2][num]['rulenum']
#             innumber = self.list[2][num]['innumber']
#             outnumber = self.list[2][num]['outnumber']
#             proname = ""
#             table = ""
#             column = ""
#             where = ""
#             # 用第三个sheet的rulenum去获取第二个sheet的规则信息
#             for n in range(len(self.list[1])):
#                 if rulenum == self.list[1][n]['rulenum']:
#                     proname = self.list[1][n]['sp']
#                     table = self.list[1][n]['table']
#                     column = self.list[1][n]['column']
#                     where = self.list[1][n]['where']
#                     findrulebiaoshi = "1"
#             # 判断第三个sheet数据是否在第二个sheet有对应规则
#             if findrulebiaoshi == "0":
#                 maphave["数据编号" + str(num + 2)] = "未匹配到对应的规则信息"
#                 self.resultcheck = "false"
#                 self.listcheck.append(maphave)
#                 continue
#
#             i = 0
#             inlist = []
#             outmap = {}
#             # 获取和设置存储过程的入参和出参
#             for all in range(int(innumber)):
#                 i += 1
#                 inlist.append(str(self.list[2][num]["value" + str(i)]))
#
#             outmap["v_flag"] = "number"
#             outmap["v_remark"] = "str"
#             tablelist = table.split(",")
#             columnlist = column.split("&")
#             wherelist = where.split(",")
#             biaoshi = "0"
#
#             # 调用存储过程
#             result = conOracle.usePro(self.url, proname, inlist, outmap)
#
#             # 验证存储过程是否调用成功
#             if result[int(innumber)] == 0.0:
#                 pass
#             else:
#                 print("<p style='color:#9400D3'>数据编号" + str(num + 2) + "的存储过程执行异常！\n</p>")
#                 continue
#             # self.assertEqual(result[int(innumber)], 0.0)
#             # self.assertEqual(result[int(innumber)+1], "成功")
#
#             sqlbiaoshi = "0"
#             checklist = []
#             # 循环获取需验证的表的信息
#             for index in range(len(tablelist)):
#                 wheres = wherelist[index].split("'")
#                 allwhere = ""
#                 for ss in wheres:
#                     if ss.isdigit():
#                         allwhere += "'" + self.list[2][num]["value" + ss] + "'"
#                     else:
#                         allwhere += ss
#                 col = columnlist[index].split(",")
#                 t1 = ""
#                 t2 = ""
#                 ind = 1
#                 for co in col:
#                     t1 += "t.a" + str(ind) + " as " + co + ","
#                     t2 += co + " as a" + str(ind) + ","
#                     ind += 1
#                 sql = "select " + t1[:-1] + " from (select " + t2[:-1] + " from " + tablelist[
#                     index] + " " + allwhere + ") t where rownum=1"
#                 resultsql = conOracle.queryOracleReturnMap(self.url, sql)
#                 if resultsql == {}:
#                     maphave["数据编号" + str(num + 2) + "的" + tablelist[index] + "表"] = "未查询到任何数据，请检查传入sql，传入sql为" + sql
#                     self.resultcheck = "false"
#                     self.listcheck.append(maphave)
#                     sqlbiaoshi = "1"
#                     maphave = {}
#                 checklist.append(resultsql)
#
#             if sqlbiaoshi == "1":
#                 continue
#
#             exceptmap = {}
#             # 获取excel中需验证的数据值
#             for number in range(int(outnumber)):
#                 i += 1
#                 forlist = str(self.list[2][num]["value" + str(i)]).split("=")
#                 exceptmap[forlist[0]] = forlist[1]
#
#             # excel
#             listzc = []
#
#             try:
#                 # 验证实际值与期望值是否一致
#                 for name in exceptmap.keys():
#                     excelishave = "0"
#                     for check in checklist:
#                         for checkname in check.keys():
#                             if name == checkname:
#                                 # excel
#                                 mapzc = {}
#                                 mapzc["指标名"] = name
#                                 mapzc["期望值"] = exceptmap[name]
#                                 mapzc["实际值"] = str(check[name])
#                                 if exceptmap[name] == "":
#                                     exceptmap[name] = "None"
#                                 if exceptmap[name] == "notNone":
#                                     if str(check[name]) == "None":
#                                         self.resultcheck = "false"
#                                         listhave.append(name + ",期望值：" + exceptmap[name] + ",实际值：" + str(check[name]))
#                                         biaoshi = "1"
#                                     excelishave = "1"
#                                 else:
#                                     if str(check[name]) != exceptmap[name] and str(check[name]) + ".0" != exceptmap[
#                                         name] and str(check[name]) != exceptmap[name] + ".0":
#                                         self.resultcheck = "false"
#                                         listhave.append(name + ",期望值：" + exceptmap[name] + ",实际值：" + str(check[name]))
#                                         biaoshi = "1"
#                                     excelishave = "1"
#                     if excelishave == "0":
#                         self.resultcheck = "false"
#                         listhave.append(name + ",该字段在excel中的column中未添加，导致该字段未做验证，请添加后重新执行")
#                         biaoshi = "1"
#                     # excel
#                     listzc.append(mapzc)
#                 if biaoshi == "1":
#                     maphave["数据编号" + str(num + 2)] = listhave
#                     self.listcheck.append(maphave)
#                 # excel
#                 mapexcel["数据编号" + str(num + 2)] = listzc
#                 self.listexcel.append(mapexcel)
#             except Exception as e:
#                 print(e)
#         # excel
#         forExcel.getExcel(self.listexcel)
#         # 打印出用例执行结果信息
#         if self.resultcheck == "true":
#             print("<p style='color:green'>测试用例执行成功!</p>")
#         else:
#             print("<p style='color:red'>测试用例执行失败!</p><p style='color:red'>失败数据详情：</p>")
#         for val in self.listcheck:
#             print("<p style='color:red'>", val, "</p>")
#         self.assertEqual("true", self.resultcheck)
