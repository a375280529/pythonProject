#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from forpub import lianghuapublic as lh
import logging

#通用存储过程场景测试
class checkLiangHua(unittest.TestCase):
    #执行前调用
    def setUp(self):
        self.resultcheck="true"
        self.ini = lh.getIni("loggerLiangHua.ini")
        self.url = self.ini["callpro"]["callproConnectUsername"] + "/" + self.ini["callpro"][
            "callproConnectPassword"] + "@" + \
                   self.ini["callpro"]["callproConnectIp"] + "/" + self.ini["callpro"]["callproConnectTable"]

    #执行后调用
    def tearDown(self):
        pass

    def test_call_pro(self):
        "量化测试"
        #values = lh.readExcelSheet("F:\\ahp\\lianghua深圳中行新.xlsx")
        values = lh.readExcelSheet(self.ini["callpro"]["callproexcelpath"])
        firstval = values[0][0]
        calname = firstval["calname"]
        intval = firstval["intval"]
        outval = firstval["outval"]
        nsrsbh = firstval["nsrsbh"]
        checktrue = firstval["checktrue"]
        checkkey = checktrue.split("&")[0]
        checkva = checktrue.split("&")[1]
        checkvalue = firstval["checkvalue"]
        mapnull = {}
        mapyuanshi = {}
        mapyuantable = {}
        mapname = {}
        for all in values[0]:
            listname = []
            if all["coulmnname"] in mapname:
                listname = mapname[all["coulmnname"]]
                listname.append(all)
                mapname[all["coulmnname"]] = listname
            else:
                listname.append(all)
                mapname[all["coulmnname"]] = listname

        initvalscore = ""
        for coulmnkeys in mapname.keys():
            mc = mapname[coulmnkeys][0]
            va = ""
            if mc["value"] != "None":
                va = mc["value"]
            initvalscore += coulmnkeys + "&" + va + "&" + mc["score"] + "&" + mc["tablename"] + ","
        initvalscore = initvalscore[:-1]

        for init in initvalscore.split(","):
            listnull = init.split("&")
            mapnull[listnull[0]] = listnull[2]
            mapyuanshi[listnull[0]] = listnull[1]
            mapyuantable[listnull[0]] = listnull[3]

        maptab = {}
        for mapyuankey in mapyuanshi.keys():
            listtab = []
            if mapyuantable[mapyuankey] in maptab.keys():
                listtab = maptab[mapyuantable[mapyuankey]]
                listtab.append(mapyuankey + "&" + mapyuanshi[mapyuankey])
                maptab[mapyuantable[mapyuankey]] = listtab
            else:
                listtab.append(mapyuankey + "&" + mapyuanshi[mapyuankey])
                maptab[mapyuantable[mapyuankey]] = listtab

        for mtkey in maptab:
            allvalues = maptab[mtkey]
            setval = ""
            for ava in allvalues:
                avaspilt = ava.split("&")
                setval += avaspilt[0] + "='" + avaspilt[1] + "',"
            setval = setval[:-1]
            sqlyuanshi = "update %s set %s where nsrsbh='%s'" % (mtkey, setval, nsrsbh)
            lh.updateOracle(self.url, sqlyuanshi)

        biaoshi = ""
        sgtable = ""
        for coulmnkeys in mapname.keys():
            if biaoshi != "" and biaoshi != mapname[coulmnkeys][0]["coulmnname"]:
                sqla = "update %s set %s='%s' where nsrsbh='%s'" % (sgtable, biaoshi, mapyuanshi[biaoshi], nsrsbh)
                lh.updateOracle(self.url, sqla)
            biaoshi = mapname[coulmnkeys][0]["coulmnname"]
            sgtable = mapname[coulmnkeys][0]["tablename"]
            for quanzhi in mapname[coulmnkeys]:
                value = ""
                if quanzhi["value"] == "None":
                    value = ''
                else:
                    value = quanzhi["value"]
                sql = "update %s set %s='%s' where nsrsbh='%s'" % (
                quanzhi["tablename"], quanzhi["coulmnname"], value, nsrsbh)
                lh.updateOracle(self.url, sql)
                inlist = []
                outmap = {}
                for inli in intval.split("&"):
                    inlist.append(str(inli))
                for outl in outval.split("&"):
                    outdou = outl.split(",")
                    outmap[outdou[0]] = outdou[1]
                result = lh.usePro(self.url, calname, inlist, outmap)
                if str(result[int(float(checkkey)) - 1]) == str(checkva) or str(
                        result[int(float(checkkey)) - 1]) == str(checkva + ".0"):
                    endscore = result[int(float(checkvalue)) - 1]
                    totalscore = 0.0
                    for mapscorekey in mapnull.keys():
                        if mapscorekey == quanzhi["coulmnname"]:
                            pass
                        else:
                            zz = mapnull[mapscorekey]
                            totalscore += float(zz)
                    totalscore += float(quanzhi["score"])
                    ts = ('%.4f' % totalscore)
                    ts = lh.quzero(ts)
                    if ts == "-0" or ts == "0":
                        ts = "0.0"
                    if ts == str(result[int(float(checkvalue)) - 1]) or ts+".0" == str(result[int(float(checkvalue)) - 1]) or ts == str(result[int(float(checkvalue)) - 1])+".0":
                        print("<p style='color:green'>"+"税号："+nsrsbh+"的"+quanzhi["coulmnname"]+"指标区间取值为"+quanzhi["value"]+"</p>")
                        print("<p style='color:green'>期望值：" + ts, "实际值:" + str(result[int(float(checkvalue)) - 1])+"</p>")
                    else:
                        print("<p style='color:red'>"+"税号："+nsrsbh+"的"+quanzhi["coulmnname"] + "指标区间取值为" + quanzhi["value"] + "时发生异常！</p>")
                        print("<p style='color:red'>期望值：" + ts, "实际值:" + str(result[int(float(checkvalue)) - 1])+"</p>")
                        self.resultcheck = "false"
                else:
                    print("<p style='color:red'>存储过程异常！</p>")
                    self.resultcheck = "false"
        #打印出用例执行结果信息
        if self.resultcheck=="true":
            print("<p style='color:green'>测试用例执行成功!</p>")
        else:
            print("<p style='color:red'>测试用例执行失败!</p>")
        self.assertEqual("true",self.resultcheck)

if __name__ == '__main__':
    unittest.main()