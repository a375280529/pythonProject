#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyclass import conOracle
from forpub import forFinal
import unittest

#sw_bg_bsry_01m变量测试正常场景
class checkSwbgbsry01m1(unittest.TestCase):
    #执行前调用
    def setUp(self):
        self.url = "vz_bz4/vz_bz4@192.168.85.81:1521/emserver"
        self.nsrsbh = "440100593700191"
        self.spsj = "2016-01-21"
        self.id = forFinal.haveIntRondom()
        self.proname = "P_BZZB_JC"
        self.inlist = []
        self.outmap = {}
        self.inlist.append(self.nsrsbh)
        self.inlist.append(self.spsj)
        self.inlist.append(self.id)
        self.outmap["v_flag"] = "number"
        self.outmap["v_remark"] = "str"
        self.bgxmmc = "办税人姓名"

    #执行后调用
    def tearDown(self):
        pass

    def test_sw_bg_bsry_01m(self):
        "sw_bg_bsry_01m变量正常场景自动化测试验证"
        result = conOracle.usePro(self.url, self.proname, self.inlist, self.outmap)
        if result[3] == 0.0:
            print("存储过程执行成功！")
        else:
            print("存储过程执行异常！")
        self.assertEqual(result[3], 0.0)

        sqlexpect = "select nvl(sum(case when bgxmmc = '%s' and bgrq > to_char(add_months(to_date('%s', 'yyyy-mm-dd'), -1),'yyyy-mm-dd') then 1 else 0 end),0) as sum_sw_bg_bsry_01m " \
                    "from (select distinct bgxmmc, bgqnr, bghnr, bgrq, bgxmdm from zx_bgdjxx where nsrsbh = '%s' and (bgqnr != bghnr or bghnr is null or bgqnr " \
                    "is null) and bgrq > to_char(add_months(to_date('%s', 'yyyy-mm-dd'), -36),'yyyy') and lrsj > (select max(lrsj) - 3 / 24 / 60 from zx_bgdjxx where " \
                    "nsrsbh = '%s'))" % (self.bgxmmc, self.spsj, self.nsrsbh, self.spsj, self.nsrsbh)
        resultexpect = conOracle.queryOracleReturnMap(self.url, sqlexpect)
        sbb01mexpect = resultexpect["SUM_SW_BG_BSRY_01M"]

        sqlresult = "select t.sw_bg_bsry_01m from (select sw_bg_bsry_01m from T_JC_ZB where nsrsbh='%s' order by lrsj desc) t where rownum=1" % (
            self.nsrsbh)
        resultreal = conOracle.queryOracleReturnMap(self.url, sqlresult)
        sbb01m = resultreal["SW_BG_BSRY_01M"]
        if sbb01mexpect == sbb01m:
            print("期望值与实际值匹配！", "期望值：" + str(sbb01mexpect), "实际值：" + str(sbb01m))
        else:
            print("期望值与实际值不匹配！", "期望值：" + str(sbb01mexpect), "实际值：" + str(sbb01m))
        self.assertEqual(sbb01mexpect, sbb01m)

if __name__ == '__main__':
    unittest.main()


