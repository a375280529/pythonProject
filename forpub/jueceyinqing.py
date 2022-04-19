#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import finalClass as fc
import jsonpath

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
        self.ff=fc.readExcelRealGeShi("D:\\juece\\juece平安额度.xlsx")

    # 执行后调用
    def tearDown(self):
        pass

    def test_call_pro(self):
        "决策引擎额度测试"
        num = 0
        for hh in self.ff:
            num += 1
            qiwrule = hh["期望命中规则"]
            try:
                qiwrulelist = qiwrule.split(";")
            except:
                pass
            result = hh["期望结果"]
            sw_jcxx_sfgtgsh = hh["sw_jcxx_sfgtgsh"]
            sw_jcxx_nsrlxdm = hh["sw_jcxx_nsrlxdm"]
            applyamount = hh["applyamount"]
            sw_sb_qbxse_24m = hh["sw_sb_qbxse_24m"]
            sw_sbzs_nsze_zzsqysds_24m = hh["sw_sbzs_nsze_zzsqysds_24m"]
            sw_sb_nsze_xfs_24m = hh["sw_sb_nsze_xfs_24m"]
            sw_sb_qbxse_12m = hh["sw_sb_qbxse_12m"]
            sw_sbzs_nsze_zzsqysds_12m = hh["sw_sbzs_nsze_zzsqysds_12m"]
            sw_sb_nsze_xfs_12m = hh["sw_sb_nsze_xfs_12m"]
            sw_sb_ynse_zzs_12m = hh["sw_sb_ynse_zzs_12m"]
            xishu = hh["xishu"]
            del hh["期望结果"]
            del hh["期望命中规则"]
            params = hh
            headers = {}
            dd = fc.getJsonForPostInterface(
                "http://192.168.86.114:9080/api/v1/engine/execute/decision?tenantId=anti_fraud_test&deploymentId="+self.id+"&collectRulesInfo=true&collectVariables=true&collectIndicatorInfo=true",
                params, headers)
            try:
                re = dd["json"]["data"]["final_result"]
                hit = jsonpath.jsonpath(dd, "$..rulesInfo[?(@.hit==True)].name")
                biaoshi = ''
                biaoz = ""
                if hit == False:
                    biaoshi = '123'
                if biaoshi == '123':
                    if result == re and re == "通过":
                        print("<p style='color:green'>" + "数据编号" + str(
                            num + 1) + ":期望值：" + result + ",实际值：" + re + "</p>")
                        if sw_jcxx_sfgtgsh == 1:
                            edu = dd["json"]["infos"]["variables"]
                            t1 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T0')].value")[0]
                            t2 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T1_XGMGTH')].value")[0]
                            t3 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T2_GTH')].value")[0]
                            t4 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T3_XGMGTH')].value")[0]
                            # t5 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name==T0)].value")
                            t6 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T5_GTH')].value")[0]
                            shouxin = edu["个体户授信额度"]
                            qiwant2 = int(sw_sb_qbxse_12m * 0.2 * xishu)
                            qiwant3 = int(sw_sb_ynse_zzs_12m * 5)
                            if fc.quzero(str(t1)) != str(applyamount):
                                print("<p style='color:red'>t1额度不正确</p>")
                                resultcheck = "false"
                                biaoz = "0"
                            if int(t2) != qiwant2:
                                print("<p style='color:red'>t2额度不正确</p>")
                                resultcheck = "false"
                                biaoz = "0"
                            if int(t3) != qiwant3:
                                print("<p style='color:red'>t3额度不正确</p>")
                                resultcheck = "false"
                                biaoz = "0"
                            if fc.quzero(str(t4)) != "200000":
                                print("<p style='color:red'>t4额度不正确</p>")
                                resultcheck = "false"
                                biaoz = "0"
                            if fc.quzero(str(t5)) != "10000":
                                print("<p style='color:red'>t5额度不正确</p>")
                                resultcheck = "false"
                                biaoz = "0"
                            qiwant6 = ((sw_sb_qbxse_12m * 0.2 * xishu * 0.7 + sw_sb_ynse_zzs_12m * 5 * 0.3) * 0.9)
                            bijiaoqiwant6 = int(qiwant6 / 1000) * 1000
                            bijiaoqiwant1 = int(t1 / 1000) * 1000
                            bijiaoqiwant4 = int(t4 / 1000) * 1000
                            lista = []
                            lista.append(bijiaoqiwant6)
                            lista.append(bijiaoqiwant1)
                            lista.append(bijiaoqiwant4)
                            li = fc.maopao(lista)
                            qiwantshouxin = li[0]
                            # if li[0]<10000:
                            #     qiwantshouxin=10000
                            # else:
                            #     qiwantshouxin=li[0]
                            if qiwantshouxin != int(t6):
                                print("<p style='color:red'>t6额度不正确</p>")
                                resultcheck = "false"
                                biaoz = "0"
                            if int(shouxin) != qiwantshouxin:
                                print("<p style='color:red'>授信额度不正确！</p>")
                                resultcheck = "false"
                                biaoz = "0"
                            if biaoz == "0":
                                print("<p style='color:red'>数据编号" + str(num + 1) + ":期望t1额度：" + str(
                                    applyamount) + ",实际t1额度：" + fc.quzero(str(t1)) + ",期望t2额度：" + str(
                                    qiwant2) + ",实际t2额度：" + str(int(t2)) + ",期望t3额度：" + str(qiwant3) + ",实际t3额度：" + str(
                                    int(t3)) + ",期望t4额度：200000,实际t4额度：" + fc.quzero(
                                    str(t4)) + ",期望t5额度：10000,实际t5额度：10000,期望t6额度：" + str(li[0]) + ",实际t6额度：" + str(
                                    int(t6)) + ",期望授信额度：" + str(qiwantshouxin) + ",实际授信额度：" + str(
                                    int(shouxin)) + "</p>")
                            else:
                                print("<p style='color:green'>数据编号" + str(num + 1) + ":期望t1额度：" + str(
                                    applyamount) + ",实际t1额度：" + fc.quzero(str(t1)) + ",期望t2额度：" + str(
                                    qiwant2) + ",实际t2额度：" + str(int(t2)) + ",期望t3额度：" + str(qiwant3) + ",实际t3额度：" + str(
                                    int(t3)) + ",期望t4额度：200000,实际t4额度：" + fc.quzero(
                                    str(t4)) + ",期望t5额度：10000,实际t5额度：10000,期望t6额度：" + str(li[0]) + ",实际t6额度：" + str(
                                    int(t6)) + ",期望授信额度：" + str(qiwantshouxin) + ",实际授信额度：" + str(
                                    int(shouxin)) + "</p>")
                        else:
                            if sw_jcxx_nsrlxdm == 1:
                                edu = dd["json"]["infos"]["variables"]
                                t1 = edu["申请额度"]
                                t2 = edu["T1_YB"]
                                t3 = edu["T2_YB"]
                                t4 = edu["T3_YB"]
                                t5 = edu["T4_YB"]
                                t6 = edu["T5_YB"]
                                shouxin = edu["一般纳税人授信额度"]
                                qiwant2 = int((sw_sb_qbxse_24m / 2) * 0.2 * xishu)
                                qiwant3 = int((sw_sbzs_nsze_zzsqysds_24m + sw_sb_nsze_xfs_24m) / 2 * 5)
                                if fc.quzero(str(t1)) != str(applyamount):
                                    print("<p style='color:red'>t1额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if int(t2) != qiwant2:
                                    print("<p style='color:red'>t2额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if int(t3) != qiwant3:
                                    print("<p style='color:red'>t3额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if fc.quzero(str(t4)) != "500000":
                                    print("<p style='color:red'>t4额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if fc.quzero(str(t5)) != "10000":
                                    print("<p style='color:red'>t5额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                qiwant6 = (((sw_sb_qbxse_24m / 2) * 0.2 * xishu * 0.7 + (
                                            sw_sbzs_nsze_zzsqysds_24m + sw_sb_nsze_xfs_24m) / 2 * 5 * 0.3) * 0.9)
                                bijiaoqiwant6 = int(qiwant6 / 1000) * 1000
                                bijiaoqiwant1 = int(t1 / 1000) * 1000
                                bijiaoqiwant4 = int(t4 / 1000) * 1000
                                lista = []
                                lista.append(bijiaoqiwant6)
                                lista.append(bijiaoqiwant1)
                                lista.append(bijiaoqiwant4)
                                li = fc.maopao(lista)
                                qiwantshouxin = li[0]
                                # if li[0] < 10000:
                                #     qiwantshouxin = 10000
                                # else:
                                #     qiwantshouxin = li[0]
                                if qiwantshouxin != int(t6):
                                    print("<p style='color:red'>t6额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if int(shouxin) != qiwantshouxin:
                                    print("<p style='color:red'>授信额度不正确！</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if biaoz == "0":
                                    print("<p style='color:red'>数据编号" + str(num + 1) + ":期望t1额度：" + str(
                                        applyamount) + ",实际t1额度：" + fc.quzero(str(t1)) + ",期望t2额度：" + str(
                                        qiwant2) + ",实际t2额度：" + str(int(t2)) + ",期望t3额度：" + str(
                                        qiwant3) + ",实际t3额度：" + str(int(t3)) + ",期望t4额度：500000,实际t4额度：" + fc.quzero(
                                        str(t4)) + ",期望t5额度：10000,实际t5额度：" + fc.quzero(str(t5)) + ",期望t6额度：" + str(
                                        qiwantshouxin) + ",实际t6额度：" + str(int(t6)) + ",期望授信额度：" + str(
                                        li[0]) + ",实际授信额度：" + str(int(shouxin)) + "</p>")
                                else:
                                    print("<p style='color:green'>数据编号" + str(num + 1) + ":期望t1额度：" + str(
                                        applyamount) + ",实际t1额度：" + fc.quzero(str(t1)) + ",期望t2额度：" + str(
                                        qiwant2) + ",实际t2额度：" + str(int(t2)) + ",期望t3额度：" + str(
                                        qiwant3) + ",实际t3额度：" + str(
                                        int(t3)) + ",期望t4额度：500000,实际t4额度：" + fc.quzero(
                                        str(t4)) + ",期望t5额度：10000,实际t5额度：" + fc.quzero(str(t5)) + ",期望t6额度：" + str(
                                        qiwantshouxin) + ",实际t6额度：" + str(int(t6)) + ",期望授信额度：" + str(
                                        li[0]) + ",实际授信额度：" + str(int(shouxin)) + "</p>")
                            else:
                                edu = dd["json"]["infos"]["variables"]
                                t1 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T0')].value")[0]
                                t2 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T1_XGMGTH')].value")[0]
                                t3 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T2_XGM')].value")[0]
                                t4 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T3_XGMGTH')].value")[0]
                                # t5 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name==T0)].value")
                                t6 = jsonpath.jsonpath(dd, "$..indicatorInfos[?(@.name=='T5_XGM')].value")[0]
                                shouxin = edu["小规模授信额度"]
                                qiwant2 = int(sw_sb_qbxse_12m * 0.2 * xishu)
                                qiwant3 = int((sw_sbzs_nsze_zzsqysds_12m + sw_sb_nsze_xfs_12m) * 5)
                                if fc.quzero(str(t1)) != str(applyamount):
                                    print("<p style='color:red'>t1额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if int(t2) != qiwant2:
                                    print("<p style='color:red'>t2额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if int(t3) != qiwant3:
                                    print("<p style='color:red'>t3额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if fc.quzero(str(t4)) != "200000":
                                    print("<p style='color:red'>t4额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if fc.quzero(str(t5)) != "10000":
                                    print("<p style='color:red'>t5额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                qiwant6 = ((sw_sb_qbxse_12m * 0.2 * xishu * 0.7 + (
                                        sw_sbzs_nsze_zzsqysds_12m + sw_sb_nsze_xfs_12m) * 5 * 0.3) * 0.9)
                                bijiaoqiwant6 = int(qiwant6 / 1000) * 1000
                                bijiaoqiwant1 = int(t1 / 1000) * 1000
                                bijiaoqiwant4 = int(t4 / 1000) * 1000
                                lista = []
                                lista.append(bijiaoqiwant6)
                                lista.append(bijiaoqiwant1)
                                lista.append(bijiaoqiwant4)
                                li = fc.maopao(lista)
                                qiwantshouxin = li[0]
                                # if li[0] < 10000:
                                #     qiwantshouxin = 10000
                                # else:
                                #     qiwantshouxin = li[0]
                                if qiwantshouxin != int(t6):
                                    print("<p style='color:red'>t6额度不正确</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if int(shouxin) != qiwantshouxin:
                                    print("<p style='color:red'>授信额度不正确！</p>")
                                    resultcheck = "false"
                                    biaoz = "0"
                                if biaoz == "0":
                                    print("<p style='color:red'>数据编号" + str(num + 1) + ":期望t1额度：" + str(
                                        applyamount) + ",实际t1额度：" + fc.quzero(str(t1)) + ",期望t2额度：" + str(
                                        qiwant2) + ",实际t2额度：" + str(int(t2)) + ",期望t3额度：" + str(
                                        qiwant3) + ",实际t3额度：" + str(int(t3)) + ",期望t4额度：200000,实际t4额度：" + fc.quzero(
                                        str(t4)) + ",期望t5额度：10000,实际t5额度：10000,期望t6额度：" + str(li[0]) + ",实际t6额度：" + str(
                                        int(t6)) + ",期望授信额度：" + str(qiwantshouxin) + ",实际授信额度：" + str(
                                        int(shouxin)) + "</p>")
                                else:
                                    print("<p style='color:green'>数据编号" + str(num + 1) + ":期望t1额度：" + str(
                                        applyamount) + ",实际t1额度：" + fc.quzero(str(t1)) + ",期望t2额度：" + str(
                                        qiwant2) + ",实际t2额度：" + str(int(t2)) + ",期望t3额度：" + str(
                                        qiwant3) + ",实际t3额度：" + str(
                                        int(t3)) + ",期望t4额度：200000,实际t4额度：" + fc.quzero(
                                        str(t4)) + ",期望t5额度：10000,实际t5额度：10000,期望t6额度：" + str(li[0]) + ",实际t6额度：" + str(
                                        int(t6)) + ",期望授信额度：" + str(qiwantshouxin) + ",实际授信额度：" + str(
                                        int(shouxin)) + "</p>")
                    else:
                        self.maphave["数据编号" + str(num + 1)] = "期望值：" + result + ",实际值：" + re
                        resultcheck = "false"
                else:
                    if result == re and re == "拒绝":
                        biao = ""
                        for qival in qiwrulelist:
                            if qival in hit:
                                pass
                            else:
                                biao = "1"
                        if biao == "":
                            print("<p style='color:green'>" + "数据编号" + str(
                                num + 1) + ":期望值：" + result + ",实际值：" + re + ",期望命中规则：" + qiwrule + ",实际命中规则：" + (
                                      ';'.join(hit)) + "</p>")
                        else:
                            self.maphave["数据编号" + str(
                                num + 1)] = "期望值：" + result + ",实际值：" + re + ",期望命中规则：" + qiwrule + ",实际命中规则：" + (
                                ';'.join(hit))
                            resultcheck = "false"
                    else:
                        self.maphave[
                            "数据编号" + str(
                                num + 1)] = "期望值：" + result + ",实际值：" + re + ",期望命中规则：" + qiwrule + ",实际命中规则：" + (
                            ';'.join(hit))
                        resultcheck = "false"
            except Exception as e:
                resultcheck = "false"
                print("<p style='color:red'>" + dd["json"]["message"] + "</p>")
        if resultcheck == "false" and self.maphave != {}:
            print("<p style='color:red'>测试用例执行失败!</p>")
            print("<p style='color:red'>失败数据详情：</p>")
            print("<p style='color:red'>" + str(self.maphave) + "</p>")
        elif resultcheck == "false":
            pass
        else:
            print("<p style='color:green'>测试用例执行成功!</p>")
        self.assertEqual("true", self.resultcheck)

if __name__ == '__main__':
    unittest.main()