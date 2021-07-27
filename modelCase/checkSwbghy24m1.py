#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyclass import conOracle
from forpub import forFinal
import unittest

#sw_bg_hy_24m变量测试正常场景
class checkSwbghy24m1(unittest.TestCase):
    #执行前调用
    def setUp(self):
        self.url = "vz_bz4/vz_bz4@192.168.85.81:1521/emserver"
        self.nsrsbh = "44142319780720271300"
        self.spsj = "2015-02-21"
        self.id = forFinal.haveIntRondom()
        self.proname = "P_BZZB_JC"
        self.inlist = []
        self.outmap = {}
        self.inlist.append(self.nsrsbh)
        self.inlist.append(self.spsj)
        self.inlist.append(self.id)
        self.outmap["v_flag"] = "number"
        self.outmap["v_remark"] = "str"
        self.bgxmmc = "'国标行业', '国标行业（附）'"

    #执行后调用
    def tearDown(self):
        pass

    def test_sw_bg_hy_24m(self):
        "sw_bg_hy_24m变量正常场景自动化测试验证"
        result = conOracle.usePro(self.url, self.proname, self.inlist, self.outmap)
        if result[3] == 0.0:
            print("存储过程执行成功！")
        else:
            print("存储过程执行异常！")
        self.assertEqual(result[3], 0.0)

        sqlexpect = "select nvl(sum(case when bgxmmc in (%s) and bgrq > to_char(add_months(to_date('%s', 'yyyy-mm-dd'), -24),'yyyy-mm-dd') then 1 else 0 end),0) as sum_sw_bg_hy_24m " \
                    "from (select distinct bgxmmc, bgqnr, bghnr, bgrq, bgxmdm from zx_bgdjxx where nsrsbh = '%s' and (bgqnr != bghnr or bghnr is null or bgqnr " \
                    "is null) and bgrq > to_char(add_months(to_date('%s', 'yyyy-mm-dd'), -36),'yyyy') and lrsj > (select max(lrsj) - 3 / 24 / 60 from zx_bgdjxx where " \
                    "nsrsbh = '%s'))" % (self.bgxmmc, self.spsj, self.nsrsbh, self.spsj, self.nsrsbh)

        resultexpect = conOracle.queryOracleReturnMap(self.url, sqlexpect)
        sbh24mexpect = resultexpect["SUM_SW_BG_HY_24M"]

        sqlresult = "select t.sw_bg_hy_24m from (select sw_bg_hy_24m from T_JC_ZB where nsrsbh='%s' order by lrsj desc) t where rownum=1" % (
            self.nsrsbh)
        resultreal = conOracle.queryOracleReturnMap(self.url, sqlresult)
        sbh24m = resultreal["SW_BG_HY_24M"]
        if sbh24mexpect == sbh24m:
            print("期望值与实际值匹配！", "期望值：" + str(sbh24mexpect), "实际值：" + str(sbh24m))
        else:
            print("期望值与实际值不匹配！", "期望值：" + str(sbh24mexpect), "实际值：" + str(sbh24m))
        self.assertEqual(sbh24mexpect, sbh24m)

if __name__ == '__main__':
    unittest.main()


