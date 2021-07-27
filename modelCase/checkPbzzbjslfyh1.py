#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyclass import conOracle,forExcel
import unittest

#p_bzzb_js_lfyh存储过程场景测试
class checkPbzzbjslfyh1(unittest.TestCase):
    #执行前调用
    def setUp(self):
        self.listcheck=[]
        self.resultcheck="true"
        self.url = "test_lfyh/test_lfyh@192.168.85.81:1521/emserver"
        self.list=forExcel.readExcel("E:\\test\\test.xlsx")
        self.proname = "P_BZZB_JS_LFYH"

    #执行后调用
    def tearDown(self):
        pass

    def test_p_bzzb_js_lfyh(self):
        "p_bzzb_js_lfyh存储过程场景测试"
        for num in range(len(self.list)):
            id = str(self.list[num]["ID"])
            nsrsbh = str(self.list[num]["NSRSBH"])
            spsj = self.list[num]["SPSJ"]
            inlist = []
            outmap = {}
            inlist.append(id)
            inlist.append(nsrsbh)
            inlist.append(spsj)
            outmap["v_flag"] = "number"
            outmap["v_remark"] = "str"

            biaoshi="0"
            maphave={}
            listhave=[]

            result = conOracle.usePro(self.url, self.proname, inlist, outmap)
            if result[3] == 0.0 and result[4] == "成功":
                pass
            else:
                print("<p>第"+str(num+1)+"次存储过程执行异常！\n</p>")

            self.assertEqual(result[3], 0.0)
            self.assertEqual(result[4], "成功")


            sql_t_sbzs_zb="select t.* from (select SW_SBZS_ZNJCS_12M_ZZSSDS,SW_SBZS_YCJNCS_03M_ZZSSDS,SW_SBZS_YCJNCS_12M_ZZSSDS,SW_SBZS_NSZE_ZZSQYSDS_24M from T_SBZS_ZB" \
                          " where nsrsbh ='%s' order by lrsj desc) t where rownum=1" %(nsrsbh)

            sql_t_jc_zb="select t.* from (select SW_JCXX_HY,SW_WFWZ_06M,SW_LXR_FRNL,SW_LXR_FRXM,SP_SJ,SW_JCXX_CLNX,SW_JCXX_NSRZTDM,SW_JCXX_NSRXYPJ,SW_JCXX_NSRLXDM from " \
                        "T_JC_ZB where nsrsbh ='%s' order by lrsj desc) t where rownum=1" %(nsrsbh)

            sql_t_sb_zb="select t.* from (select SW_SB_SFL_ZZSQYSDS_12M_A,SW_SB_SFLHY_A,SW_SB_SCSB,SW_SB_QBXSE_12M,SW_SB_QBXSEHBZZL_03M_A,SW_SB_QBXSEZZL_06M_A,SW_SB_QBXSEZZL_12M_A" \
                        ",SW_SB_ZDLXSB0_24M,SW_SB_LJSB0_24M,SW_SB_QBXSEZZL_03M,SW_SB_LSXS_12M,SW_SB_LJSB0_03Q,SW_SB_QBXSE_02Q,SW_SB_QBXSEHBZZL_03M,SW_SB_QBXSEZZL_06M," \
                        "SW_SB_QBXSEZZL_12M,SW_SB_LJSB0_12M,SW_SB_ZDLXSB0_12M,SW_SB_NSZE_ZZSQYSDS_12M,SW_SB_YQWSB,SW_SB_QBXSE_24M,SW_SB_NSZEZZL_ZZSQYSDS_12M_A," \
                        "SW_SB_NSZEZZL_ZZSQYSDS_06M from T_SB_ZB where nsrsbh ='%s' order by lrsj desc) t where rownum=1" %(nsrsbh)

            sql_t_lrb_xm="select t.* from (select SW_CWBB_JLR_1 from T_LRB_XM  where nsrsbh ='%s' order by lrsj desc) t where rownum=1" %(nsrsbh)

            sql_t_cwbb_zb="select t.* from (select SW_CWBB_LRSRBL_A,SW_CWBB_YXZCZWL,SW_CWBB_LDFZYYSR_QJ,SW_CWBB_JLRSYZQY_QJ,SW_CWBB_XSJLL from T_CWBB_ZB where " \
                          "nsrsbh ='%s' order by lrsj desc) t where rownum=1" %(nsrsbh)

            sql_t_zcfzb_xm="select t.* from (select SW_CWBB_SYZQY_1 from T_ZCFZB_XM where nsrsbh ='%s' order by lrsj desc) t where rownum=1" %(nsrsbh)

            result_t_sbzs_zb=conOracle.queryOracleReturnMap(self.url, sql_t_sbzs_zb)

            result_t_jc_zb = conOracle.queryOracleReturnMap(self.url, sql_t_jc_zb)

            result_t_sb_zb = conOracle.queryOracleReturnMap(self.url, sql_t_sb_zb)

            result_t_lrb_xm = conOracle.queryOracleReturnMap(self.url, sql_t_lrb_xm)

            result_t_cwbb_zb = conOracle.queryOracleReturnMap(self.url, sql_t_cwbb_zb)

            result_t_zcfzb_xm = conOracle.queryOracleReturnMap(self.url, sql_t_zcfzb_xm)

            try:
                for name in self.list[num].keys():
                    if name =="SW_SBZS_ZNJCS_12M_ZZSSDS" or name == "SW_SBZS_YCJNCS_03M_ZZSSDS" or name == "SW_SBZS_YCJNCS_12M_ZZSSDS" or name == "SW_SBZS_NSZE_ZZSQYSDS_24M":
                        if str(result_t_sbzs_zb[name]) != self.list[num][name]:
                            self.resultcheck="false"
                            listhave.append(name+",期望值："+self.list[num][name]+",实际值："+str(result_t_sbzs_zb[name]))
                            biaoshi = "1"
                    elif name =="SW_JCXX_HY" or name == "SW_WFWZ_06M" or name == "SW_LXR_FRNL" or name == "SW_LXR_FRXM" or name == "SP_SJ" or name == "SW_JCXX_CLNX" \
                            or name == "SW_JCXX_NSRZTDM" or name == "SW_JCXX_NSRXYPJ" or name == "SW_JCXX_NSRLXDM":
                        if name=="SW_JCXX_NSRZTDM":
                            if self.list[num][name]!=str(None) and self.list[num][name]!="0":
                                self.list[num][name]="0"+self.list[num][name]
                        if str(result_t_jc_zb[name]) != self.list[num][name]:
                            self.resultcheck = "false"
                            listhave.append(name+",期望值："+self.list[num][name]+",实际值："+str(result_t_jc_zb[name]))
                            biaoshi = "1"
                    elif name =="SW_SB_SFL_ZZSQYSDS_12M_A" or name == "SW_SB_SFLHY_A" or name == "SW_SB_SCSB" or name == "SW_SB_QBXSE_12M" or name == "SW_SB_QBXSEHBZZL_03M_A" or name == "SW_SB_QBXSEZZL_06M_A" \
                            or name == "SW_SB_QBXSEZZL_12M_A" or name == "SW_SB_ZDLXSB0_24M" or name == "SW_SB_LJSB0_24M" or name == "SW_SB_QBXSEZZL_03M" or name == "SW_SB_LSXS_12M" \
                            or name == "SW_SB_LJSB0_03Q" or name == "SW_SB_QBXSE_02Q" or name == "SW_SB_QBXSEHBZZL_03M" or name == "SW_SB_QBXSEZZL_06M" or name == "SW_SB_QBXSEZZL_12M" \
                            or name == "SW_SB_LJSB0_12M" or name == "SW_SB_ZDLXSB0_12M" or name == "SW_SB_NSZE_ZZSQYSDS_12M" or name == "SW_SB_YQWSB" or name == "SW_SB_QBXSE_24M" \
                            or name == "SW_SB_NSZEZZL_ZZSQYSDS_12M_A" or name == "SW_SB_NSZEZZL_ZZSQYSDS_06M":
                        if str(result_t_sb_zb[name]) != self.list[num][name]:
                            self.resultcheck = "false"
                            listhave.append(name+",期望值："+self.list[num][name]+",实际值："+str(result_t_sb_zb[name]))
                            biaoshi = "1"
                    elif name =="SW_CWBB_JLR_1":
                        if str(result_t_lrb_xm[name]) != self.list[num][name]:
                            self.resultcheck = "false"
                            listhave.append(name+",期望值："+self.list[num][name]+",实际值："+str(result_t_lrb_xm[name]))
                            biaoshi = "1"
                    elif name =="SW_CWBB_LRSRBL_A" or name == "SW_CWBB_YXZCZWL" or name == "SW_CWBB_LDFZYYSR_QJ" or name == "SW_CWBB_JLRSYZQY_QJ" or name == "SW_CWBB_XSJLL":
                        if str(result_t_cwbb_zb[name]) != self.list[num][name]:
                            self.resultcheck = "false"
                            listhave.append(name+",期望值："+self.list[num][name]+",实际值："+str(result_t_cwbb_zb[name]))
                            biaoshi = "1"
                    elif name =="SW_CWBB_SYZQY_1":
                        if str(result_t_zcfzb_xm[name]) != self.list[num][name]:
                            self.resultcheck = "false"
                            listhave.append(name+",期望值："+self.list[num][name]+",实际值："+str(result_t_zcfzb_xm[name]))
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


