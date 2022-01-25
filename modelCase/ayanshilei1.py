#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from pyclass import conOracle,getInterface
from forpub import forFinal


#通用存储过程场景测试
class checkCallProNew(unittest.TestCase):
    #执行前调用
    def setUp(self):
        self.nsrsbh = "cs1593572468"
        self.resultcheck = "true"
        self.ini = forFinal.getIni("loggeryanshi.ini")
        self.url = self.ini["callpro"]["callproConnectUsername"] + "/" + self.ini["callpro"][
            "callproConnectPassword"] + "@" + \
                   self.ini["callpro"]["callproConnectIp"] + "/" + self.ini["callpro"]["callproConnectTable"]

    #执行后调用
    def tearDown(self):
        #数据恢复
        sqlhui="delete from zx_nsrjcxx where nsrsbh='%s'"%(self.nsrsbh)
        conOracle.updateOracle(self.url, sqlhui)

    def test_call_pro(self):
        "演示测试"
        url="http://192.168.87.65:8080/jkzdh?nsrsbh=%s"%(self.nsrsbh)
        res=getInterface.getJsonForGetInterface(url,{},{})
        msg=res.get("json").get("msg")
        if msg!="成功":
            out="<p style='color:red'>msg返回%s</p>"%(msg)
            print(out)
        self.assertEqual("true", self.resultcheck)
        sql="select count(1) as num from zx_nsrjcxx where nsrsbh='%s'"%(self.nsrsbh)
        ma=conOracle.queryOracleReturnMap(self.url,sql)
        if ma.get("NUM")==0:
            self.resultcheck = "fasle"
            print("<p style='color:red'>数据插入异常</p>")
        self.assertEqual("true", self.resultcheck)
        print("<p style='color:green'>用例执行成功</p>")

    def test_call_pro1(self):
        "演示测试"
        url="http://192.168.87.65:8080/jkzdh?nsr=%s"%(self.nsrsbh)
        res=getInterface.getJsonForGetInterface(url,{},{})
        msg=res.get("json").get("msg")
        if msg!="成功":
            out="<p style='color:red'>msg返回%s</p>"%(msg)
            print(out)
        self.assertEqual("true", self.resultcheck)
        sql="select count(1) as num from zx_nsrjcxx where nsrsbh='%s'"%(self.nsrsbh)
        ma=conOracle.queryOracleReturnMap(self.url,sql)
        if ma.get("NUM")==0:
            self.resultcheck = "fasle"
            print("<p style='color:red'>数据插入异常</p>")
        self.assertEqual("true", self.resultcheck)
        print("<p style='color:green'>用例执行成功</p>")

if __name__ == '__main__':
    unittest.main()