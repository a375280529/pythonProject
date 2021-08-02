#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import finalClass as fc

# 通用存储过程场景测试
class text(unittest.TestCase):
    # 执行前调用
    def setUp(self):
        self.resultcheck = "true"
        self.maphave = {}
        self.ini = fc.getIni("logger.ini")
        self.id = self.ini["juece"]["id"]
        self.exepath = os.path.realpath(sys.executable)
        self.endpath = self.exepath.split(self.exepath.split("\\")[-1])[0]
        self.exclepath = os.path.join(os.path.abspath('.'), self.endpath + "juece.xlsx")
        self.ff=fc.readExcelRealGeShi("D:\\juece\\juece.xlsx")

    # 执行后调用
    def tearDown(self):
        pass

    def test_call_pro(self):
        "决策引擎测试"
        num = 0
        for hh in self.ff:
            num += 1
            result = hh["期望结果"]
            del hh["期望结果"]
            params = hh
            headers = {}
            dd = fc.getJsonForPostInterface(
                "http://192.168.86.114:9080/api/v1/engine/execute/decision?tenantId=anti_fraud_test&deploymentId=" + self.id + "&collectRulesInfo=true&collectVariables=true&collectIndicatorInfo=true&collectVariables=true",
                params, headers)
            #print(dd)
            try:
                re = dd["json"]["data"]["final_result"]
                if result == re:
                    pass
                else:
                    self.maphave["数据编号" + str(num + 1)] = "期望值：" + result + ",实际值：" + re
                    self.resultcheck = "false"
            except Exception as e:
                self.resultcheck = "false"
                print("<p style='color:red'>" + dd["json"]["message"] + "</p>")
        if self.resultcheck == "false" and self.maphave != {}:
            print("<p style='color:red'>测试用例执行失败!</p>")
            print("<p style='color:red'>失败数据详情：</p>")
            print("<p style='color:red'>" + str(self.maphave) + "</p>")
        elif self.resultcheck == "false":
            pass
        else:
            print("<p style='color:green'>测试用例执行成功!</p>")
        self.assertEqual("true", self.resultcheck)

if __name__ == '__main__':
    unittest.main()