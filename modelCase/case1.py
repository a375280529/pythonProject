#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyclass import conOracle,forText,forExcel

#获取表名
def haveKey(rulealls,maptest):
    for tablename in maptest.keys():
        if rulealls in maptest[tablename]:
            return tablename

#验证单条件的方法
def checkRule(ruleall,result):
    realvalue = result[ruleall[5]]
    rule0 = ruleall[0]
    rule1 = ruleall[1]
    rule2 = ruleall[2]
    rule3 = ruleall[3]
    rule4 = ruleall[4]
    rule5 = ruleall[5]
    map={}
    if realvalue is None:
        map[rule0]=rule3+": "+",&"+rule5
    else:
        if rule2.strip() == "=":
            if float(realvalue) != float(rule1):
                map[rule0]=rule3+":"+str(realvalue)+",&"+rule5
                return map
        elif rule2.strip() == ">":
            if float(realvalue) <= float(rule1):
                map[rule0]=rule3+":"+str(realvalue)+",&"+rule5
                return map
        elif rule2.strip() == "<":
            if float(realvalue) >= float(rule1):
                map[rule0]=rule3+":"+str(realvalue)+",&"+rule5
                return map
        elif rule2.strip() == ">=":
            if float(realvalue) < float(rule1):
                map[rule0]=rule3+":"+str(realvalue)+",&"+rule5
                return map
        elif rule2.strip() == "<=":
            if float(realvalue) > float(rule1):
                map[rule0]=rule3+":"+str(realvalue)+",&"+rule5
                return map
        elif rule2.strip() == "<>":
            if float(realvalue) == float(rule1):
                map[rule0]=rule3+":"+str(realvalue)+",&"+rule5
                return map
        elif rule2.strip() == "not in":
            if realvalue in rule1:
                map[rule0]=rule3+":"+str(realvalue)+",&"+rule5
                return map
    return map

#验证多条件或和且的方法
def checkMoreRule(maptest,rulesingle,result1,result2,result3,result4,result5,result6,result7):
    haveRuleList=[]
    checkIsGet=[]
    biaoshilist=[]
    biaoshi="1"
    for ruleall in rulesingle:
        tablename = haveKey(ruleall[5], maptest)
        map={}
        if ruleall[4]=="或":
            if "T_JC_ZB" == tablename:
                if len(checkRule(ruleall, result1)) > 0:
                    checkIsGet.append(checkRule(ruleall, result1))
                    biaoshilist.append("1")
                else:
                    biaoshilist.append("0")
            elif "T_ZCFZB_XM" == tablename:
                if len(checkRule(ruleall, result2)) > 0:
                    checkIsGet.append(checkRule(ruleall, result2))
                    biaoshilist.append("1")
                else:
                    biaoshilist.append("0")
            elif "T_SBZS_ZB" == tablename:
                if len(checkRule(ruleall, result3)) > 0:
                    checkIsGet.append(checkRule(ruleall, result3))
                    biaoshilist.append("1")
                else:
                    biaoshilist.append("0")
            elif "T_SB_ZB" == tablename:
                if len(checkRule(ruleall, result4)) > 0:
                    checkIsGet.append(checkRule(ruleall, result4))
                    biaoshilist.append("1")
                else:
                    biaoshilist.append("0")
            elif "T_CWBB_ZB" == tablename:
                if len(checkRule(ruleall, result5)) > 0:
                    checkIsGet.append(checkRule(ruleall, result5))
                    biaoshilist.append("1")
                else:
                    biaoshilist.append("0")
            elif "T_GSSF_ZB_HSJ" == tablename:
                if len(checkRule(ruleall, result6)) > 0:
                    checkIsGet.append(checkRule(ruleall, result6))
                    biaoshilist.append("1")
                else:
                    biaoshilist.append("0")
            elif "FH_SF_ZB" == tablename:
                if len(checkRule(ruleall, result7)) > 0:
                    checkIsGet.append(checkRule(ruleall, result7))
                    biaoshilist.append("1")
                else:
                    biaoshilist.append("0")
            # else:
            #     haveRuleList.append({"erro": ruleall[0] + "未找到对应表"})
            #     biaoshi.append("1")
        elif ruleall[4]=="且":
            if "T_JC_ZB" == tablename:
                if len(checkRule(ruleall, result1)) > 0:
                    haveRuleList.append(checkRule(ruleall, result1))
            elif "T_ZCFZB_XM" == tablename:
                if len(checkRule(ruleall, result2)) > 0:
                    haveRuleList.append(checkRule(ruleall, result2))
            elif "T_SBZS_ZB" == tablename:
                if len(checkRule(ruleall, result3)) > 0:
                    haveRuleList.append(checkRule(ruleall, result3))
            elif "T_SB_ZB" == tablename:
                if len(checkRule(ruleall, result4)) > 0:
                    haveRuleList.append(checkRule(ruleall, result4))
            elif "T_CWBB_ZB" == tablename:
                if len(checkRule(ruleall, result5)) > 0:
                    haveRuleList.append(checkRule(ruleall, result5))
            elif "T_GSSF_ZB_HSJ" == tablename:
                if len(checkRule(ruleall, result6)) > 0:
                    haveRuleList.append(checkRule(ruleall, result6))
            elif "FH_SF_ZB" == tablename:
                if len(checkRule(ruleall, result7)) > 0:
                    haveRuleList.append(checkRule(ruleall, result7))
            # else:
            #     haveRuleList.append({"erro": ruleall[0] + "未找到对应表"})
    for biao in biaoshilist:
        if biao=="0":
            biaoshi="0"
    if biaoshi=="1":
        allcheck=[]
        for check in checkIsGet:
            allcheck.append(check)
        if len(allcheck)>0:
            haveRuleList.append(allcheck)
    return haveRuleList

#根据nsrsbh获取命中规则数组
def getToRule(nsrsbh):
    maptest = {
        "T_JC_ZB": "SW_JCXX_DQJRBS,SW_JCXX_NSRLXDM,SW_LXR_FRNL,SW_JCXX_NSRXYPJ,SW_JCXX_HYJRBS,SW_JCXX_NSRZTDM,SW_JCXX_CLNX",
        "T_ZCFZB_XM": "SW_CWBB_SYZQY_1", "T_SBZS_ZB": "SW_SBZS_YCJNCS_03M_03DZSDS,"
                                                      "SW_SBZS_SSFK_12M,SW_SBZS_XWFK_12M,SW_SBZS_ZNJCS_12M_ZZSSDS,SW_SBZS_ZNJCS_06M_ZZSSDS,SW_SBZS_QS,SW_SBZS_NSZE_ZZSQYSDS_12M",
        "T_SB_ZB": "SW_SB_YQWSB,SW_SB_QBXSE_12M,"
                   "SW_SB_ZDLXSB0_12M,SW_SB_LJSB0_12M,SW_SB_ZDLXSB0_24M,SW_SB_LJSB0_24M,SW_SB_QBXSEZZL_12M,SW_SB_QBXSEZZL_06M,SW_SB_QBXSEHBZZL_03M,SW_SB_QBXSE_02Q,"
                   "SW_SB_SCSB", "T_CWBB_ZB": "SW_CWBB_XSJLL",
        "T_GSSF_ZB_HSJ": "GS_FR_CGSC,GS_YYZT,GS_BGCS_FR_2Y,GS_BGCS_FR_6M,GS_TZBL_FR", "FH_SF_ZB": "SF_FH_JRQK_BG_2Y_GR,"
                                                                                                  "SF_FH_JRQK_BG_2Y_QY,SF_FH_SXR_5Y_GR,SF_FH_SXR_5Y_QY,SF_FH_SXR_3Y_GR,SF_FH_SXR_3Y_QY,SF_FH_BZXR_3Y_GR,SF_FH_BZXR_3Y_QY,SF_FH_BZXR_1Y_GR,SF_FH_BZXR_1Y_QY"}
    result = conOracle.queryOracle("test_lfyh/test_lfyh@192.168.85.81:1521/emserver",
                         "select rule_no,rule_limit,direction,rule_description,same_or,index_dm from TAX_RULE_SET_INFO_LFYH_DQ where flag='1' and rule_type!='ZX' order by rule_no desc")
    sql1 = "select t.SW_JCXX_DQJRBS,t.SW_JCXX_NSRLXDM,t.SW_LXR_FRNL,t.SW_JCXX_NSRXYPJ,t.SW_JCXX_HYJRBS,t.SW_JCXX_NSRZTDM,t.SW_JCXX_CLNX from (select * from T_JC_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql2 = "select t.SW_CWBB_SYZQY_1 from (select * from T_ZCFZB_XM where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql3 = "select t.SW_SBZS_YCJNCS_03M_03DZSDS,t.SW_SBZS_SSFK_12M,t.SW_SBZS_XWFK_12M,t.SW_SBZS_ZNJCS_12M_ZZSSDS,t.SW_SBZS_ZNJCS_06M_ZZSSDS,t.SW_SBZS_QS,t.SW_SBZS_NSZE_ZZSQYSDS_12M from (select * from T_SBZS_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql4 = "select t.SW_SB_YQWSB,t.SW_SB_QBXSE_12M,t.SW_SB_ZDLXSB0_12M,t.SW_SB_LJSB0_12M,t.SW_SB_ZDLXSB0_24M,t.SW_SB_LJSB0_24M,t.SW_SB_QBXSEZZL_12M,t.SW_SB_QBXSEZZL_06M,t.SW_SB_QBXSEHBZZL_03M,t.SW_SB_QBXSE_02Q,t.SW_SB_SCSB from (select * from T_SB_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql5 = "select t.SW_CWBB_XSJLL from (select * from T_CWBB_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql6 = "select t.GS_FR_CGSC,t.GS_YYZT,t.GS_BGCS_FR_2Y,t.GS_BGCS_FR_6M,t.GS_TZBL_FR from (select * from T_GSSF_ZB_HSJ where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql7 = "select t.SF_FH_JRQK_BG_2Y_GR,t.SF_FH_JRQK_BG_2Y_QY,t.SF_FH_SXR_5Y_GR,t.SF_FH_SXR_5Y_QY,t.SF_FH_SXR_3Y_GR,t.SF_FH_SXR_3Y_QY,t.SF_FH_BZXR_3Y_GR,t.SF_FH_BZXR_3Y_QY,t.SF_FH_BZXR_1Y_GR,t.SF_FH_BZXR_1Y_QY from (select * from FH_SF_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"

    result1 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql1)
    result2 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql2)
    result3 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql3)
    result4 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql4)
    result5 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql5)
    result6 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql6)
    result7 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql7)

    map1 = {}
    haveRuleList = []
    for rules in result:
        forrule = rules[0].split("_")
        list1 = []
        list1.append(rules)
        if forrule[0] in map1.keys():
            for ma in map1.get(forrule[0]):
                list1.append(ma)
            map1[forrule[0]] = list1
        else:
            map1[forrule[0]] = list1
    for rulesingle in map1.keys():
        if len(map1.get(rulesingle)) > 1:
            list = checkMoreRule(maptest, map1.get(rulesingle), result1, result2, result3, result4, result5, result6,
                                 result7)
            for li in list:
                haveRuleList.append(li)
        else:
            for ruleall in map1.get(rulesingle):
                tablename = haveKey(ruleall[5], maptest)
                if "T_JC_ZB" == tablename:
                    if len(checkRule(ruleall, result1)) > 0:
                        haveRuleList.append(checkRule(ruleall, result1))
                elif "T_ZCFZB_XM" == tablename:
                    if len(checkRule(ruleall, result2)) > 0:
                        haveRuleList.append(checkRule(ruleall, result2))
                elif "T_SBZS_ZB" == tablename:
                    if len(checkRule(ruleall, result3)) > 0:
                        haveRuleList.append(checkRule(ruleall, result3))
                elif "T_SB_ZB" == tablename:
                    if len(checkRule(ruleall, result4)) > 0:
                        haveRuleList.append(checkRule(ruleall, result4))
                elif "T_CWBB_ZB" == tablename:
                    if len(checkRule(ruleall, result5)) > 0:
                        haveRuleList.append(checkRule(ruleall, result5))
                elif "T_GSSF_ZB_HSJ" == tablename:
                    if len(checkRule(ruleall, result6)) > 0:
                        haveRuleList.append(checkRule(ruleall, result6))
                elif "FH_SF_ZB" == tablename:
                    if len(checkRule(ruleall, result7)) > 0:
                        haveRuleList.append(checkRule(ruleall, result7))
                # else:
                #     haveRuleList.append({"erro":ruleall[0]+"未找到对应表"})
    return haveRuleList

def getHaveRules(nsrsbh):
    maptest = {
        "T_JC_ZB": "SW_JCXX_DQJRBS,SW_JCXX_NSRLXDM,SW_LXR_FRNL,SW_JCXX_NSRXYPJ,SW_JCXX_HYJRBS,SW_JCXX_NSRZTDM,SW_JCXX_CLNX",
        "T_ZCFZB_XM": "SW_CWBB_SYZQY_1", "T_SBZS_ZB": "SW_SBZS_YCJNCS_03M_03DZSDS,"
                                                      "SW_SBZS_SSFK_12M,SW_SBZS_XWFK_12M,SW_SBZS_ZNJCS_12M_ZZSSDS,SW_SBZS_ZNJCS_06M_ZZSSDS,SW_SBZS_QS,SW_SBZS_NSZE_ZZSQYSDS_12M",
        "T_SB_ZB": "SW_SB_YQWSB,SW_SB_QBXSE_12M,"
                   "SW_SB_ZDLXSB0_12M,SW_SB_LJSB0_12M,SW_SB_ZDLXSB0_24M,SW_SB_LJSB0_24M,SW_SB_QBXSEZZL_12M,SW_SB_QBXSEZZL_06M,SW_SB_QBXSEHBZZL_03M,SW_SB_QBXSE_02Q,"
                   "SW_SB_SCSB", "T_CWBB_ZB": "SW_CWBB_XSJLL",
        "T_GSSF_ZB_HSJ": "GS_FR_CGSC,GS_YYZT,GS_BGCS_FR_2Y,GS_BGCS_FR_6M,GS_TZBL_FR", "FH_SF_ZB": "SF_FH_JRQK_BG_2Y_GR,"
                                                                                                  "SF_FH_JRQK_BG_2Y_QY,SF_FH_SXR_5Y_GR,SF_FH_SXR_5Y_QY,SF_FH_SXR_3Y_GR,SF_FH_SXR_3Y_QY,SF_FH_BZXR_3Y_GR,SF_FH_BZXR_3Y_QY,SF_FH_BZXR_1Y_GR,SF_FH_BZXR_1Y_QY"}
    result = conOracle.queryOracle("test_lfyh/test_lfyh@192.168.85.81:1521/emserver",
                         "select rule_no,rule_limit,direction,rule_description,same_or,index_dm from TAX_RULE_SET_INFO_LFYH_DQ where flag='1' and rule_type!='ZX' order by rule_no desc")
    sql1 = "select t.SW_JCXX_DQJRBS,t.SW_JCXX_NSRLXDM,t.SW_LXR_FRNL,t.SW_JCXX_NSRXYPJ,t.SW_JCXX_HYJRBS,t.SW_JCXX_NSRZTDM,t.SW_JCXX_CLNX from (select * from T_JC_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql2 = "select t.SW_CWBB_SYZQY_1 from (select * from T_ZCFZB_XM where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql3 = "select t.SW_SBZS_YCJNCS_03M_03DZSDS,t.SW_SBZS_SSFK_12M,t.SW_SBZS_XWFK_12M,t.SW_SBZS_ZNJCS_12M_ZZSSDS,t.SW_SBZS_ZNJCS_06M_ZZSSDS,t.SW_SBZS_QS,t.SW_SBZS_NSZE_ZZSQYSDS_12M from (select * from T_SBZS_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql4 = "select t.SW_SB_YQWSB,t.SW_SB_QBXSE_12M,t.SW_SB_ZDLXSB0_12M,t.SW_SB_LJSB0_12M,t.SW_SB_ZDLXSB0_24M,t.SW_SB_LJSB0_24M,t.SW_SB_QBXSEZZL_12M,t.SW_SB_QBXSEZZL_06M,t.SW_SB_QBXSEHBZZL_03M,t.SW_SB_QBXSE_02Q,t.SW_SB_SCSB from (select * from T_SB_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql5 = "select t.SW_CWBB_XSJLL from (select * from T_CWBB_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql6 = "select t.GS_FR_CGSC,t.GS_YYZT,t.GS_BGCS_FR_2Y,t.GS_BGCS_FR_6M,t.GS_TZBL_FR from (select * from T_GSSF_ZB_HSJ where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"
    sql7 = "select t.SF_FH_JRQK_BG_2Y_GR,t.SF_FH_JRQK_BG_2Y_QY,t.SF_FH_SXR_5Y_GR,t.SF_FH_SXR_5Y_QY,t.SF_FH_SXR_3Y_GR,t.SF_FH_SXR_3Y_QY,t.SF_FH_BZXR_3Y_GR,t.SF_FH_BZXR_3Y_QY,t.SF_FH_BZXR_1Y_GR,t.SF_FH_BZXR_1Y_QY from (select * from FH_SF_ZB where nsrsbh='" + nsrsbh + "' order by lrsj desc) t where rownum=1"

    result1 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql1)
    result2 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql2)
    result3 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql3)
    result4 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql4)
    result5 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql5)
    result6 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql6)
    result7 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql7)

    map1 = {}
    haveRuleList = []
    for rules in result:
        forrule = rules[0].split("_")
        list1 = []
        list1.append(rules)
        if forrule[0] in map1.keys():
            for ma in map1.get(forrule[0]):
                list1.append(ma)
            map1[forrule[0]] = list1
        else:
            map1[forrule[0]] = list1
    for rulesingle in map1.keys():
        if len(map1.get(rulesingle)) > 1:
            list = checkMoreRule(maptest, map1.get(rulesingle), result1, result2, result3, result4, result5, result6,
                                 result7)
            for li in list:
                haveRuleList.append(li)
        else:
            for ruleall in map1.get(rulesingle):
                tablename = haveKey(ruleall[5], maptest)
                if "T_JC_ZB" == tablename:
                    if len(checkRule(ruleall, result1)) > 0:
                        haveRuleList.append(checkRule(ruleall, result1))
                elif "T_ZCFZB_XM" == tablename:
                    if len(checkRule(ruleall, result2)) > 0:
                        haveRuleList.append(checkRule(ruleall, result2))
                elif "T_SBZS_ZB" == tablename:
                    if len(checkRule(ruleall, result3)) > 0:
                        haveRuleList.append(checkRule(ruleall, result3))
                elif "T_SB_ZB" == tablename:
                    if len(checkRule(ruleall, result4)) > 0:
                        haveRuleList.append(checkRule(ruleall, result4))
                elif "T_CWBB_ZB" == tablename:
                    if len(checkRule(ruleall, result5)) > 0:
                        haveRuleList.append(checkRule(ruleall, result5))
                elif "T_GSSF_ZB_HSJ" == tablename:
                    if len(checkRule(ruleall, result6)) > 0:
                        haveRuleList.append(checkRule(ruleall, result6))
                elif "FH_SF_ZB" == tablename:
                    if len(checkRule(ruleall, result7)) > 0:
                        haveRuleList.append(checkRule(ruleall, result7))
                # else:
                #     haveRuleList.append({"erro":ruleall[0]+"未找到对应表"})
    for rulelist in haveRuleList:
        print(nsrsbh,rulelist)
        #forText.writeTxt(rulelist)

def getTestCaseMessage(nsrsbh):
    sql1 = "select t.* from (select sp_sj as SPSJ,SW_SBZS_ZNJCS_12M_ZZSSDS,SW_SBZS_YCJNCS_03M_ZZSSDS,SW_SBZS_YCJNCS_12M_ZZSSDS,SW_SBZS_NSZE_ZZSQYSDS_24M from T_SBZS_ZB where nsrsbh ='%s' order by lrsj desc) t where rownum=1" % (
        nsrsbh)
    sql2 = "select t.* from (select SW_JCXX_HY,SW_WFWZ_06M,SW_LXR_FRNL,SW_LXR_FRXM,SP_SJ,SW_JCXX_CLNX,SW_JCXX_NSRZTDM,SW_JCXX_NSRXYPJ,SW_JCXX_NSRLXDM from T_JC_ZB where nsrsbh ='%s' order by lrsj desc) t where rownum=1" % (
        nsrsbh)
    sql3 = "select t.* from (select SW_SB_SFL_ZZSQYSDS_12M_A,SW_SB_SFLHY_A,SW_SB_SCSB,SW_SB_QBXSE_12M,SW_SB_QBXSEHBZZL_03M_A,SW_SB_QBXSEZZL_06M_A,SW_SB_QBXSEZZL_12M_A,SW_SB_ZDLXSB0_24M,SW_SB_LJSB0_24M,SW_SB_QBXSEZZL_03M,SW_SB_LSXS_12M,SW_SB_LJSB0_03Q,SW_SB_QBXSE_02Q,SW_SB_QBXSEHBZZL_03M,SW_SB_QBXSEZZL_06M,SW_SB_QBXSEZZL_12M,SW_SB_LJSB0_12M,SW_SB_ZDLXSB0_12M,SW_SB_NSZE_ZZSQYSDS_12M,SW_SB_YQWSB,SW_SB_QBXSE_24M from T_SB_ZB where nsrsbh ='%s' order by lrsj desc) t where rownum=1" % (
        nsrsbh)
    sql4 = "select t.* from (select SW_CWBB_JLR_1 from T_LRB_XM  where nsrsbh ='%s' order by lrsj desc) t where rownum=1" % (
        nsrsbh)
    sql5 = "select t.* from (select SW_CWBB_LRSRBL_A,SW_CWBB_YXZCZWL,SW_CWBB_LDFZYYSR_QJ,SW_CWBB_JLRSYZQY_QJ,SW_CWBB_XSJLL from T_CWBB_ZB where nsrsbh ='%s' order by lrsj desc) t where rownum=1" % (
        nsrsbh)
    sql6 = "select t.* from (select SW_CWBB_SYZQY_1 from T_ZCFZB_XM where nsrsbh ='%s' order by lrsj desc) t where rownum=1" % (
        nsrsbh)

    result1 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql1)
    result2 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql2)
    result3 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql3)
    result4 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql4)
    result5 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql5)
    result6 = conOracle.queryOracleReturnMap("test_lfyh/test_lfyh@192.168.85.81:1521/emserver", sql6)

    listone = []
    mapone = {}
    mapone["指标名"] = 'NSRSBH'
    mapone["指标值"] = nsrsbh
    listone.append(mapone)
    # 指标名，指标值 nsrsbh
    for result in result1.keys():
        maptwo = {}
        maptwo["指标名"] = result
        maptwo["指标值"] = result1[result]
        listone.append(maptwo)
    for result in result2.keys():
        maptwo = {}
        maptwo["指标名"] = result
        maptwo["指标值"] = result2[result]
        listone.append(maptwo)
    for result in result3.keys():
        maptwo = {}
        maptwo["指标名"] = result
        maptwo["指标值"] = result3[result]
        listone.append(maptwo)
    for result in result4.keys():
        maptwo = {}
        maptwo["指标名"] = result
        maptwo["指标值"] = result4[result]
        listone.append(maptwo)
    for result in result5.keys():
        maptwo = {}
        maptwo["指标名"] = result
        maptwo["指标值"] = result5[result]
        listone.append(maptwo)
    for result in result6.keys():
        maptwo = {}
        maptwo["指标名"] = result
        maptwo["指标值"] = result6[result]
        listone.append(maptwo)

    mapt = {}
    listall = []
    mapt[nsrsbh] = listone
    listall.append(mapt)
    return listall

if __name__ == '__main__':
    #nsrsbh=ini.forGetIni.getIni("logger.ini")["model"]["nsrsbh"]
    nsrsbhs=['911320823201699999','913307005669107196','91131082320169999C']
    listall=[]
    for ns in nsrsbhs:
        getHaveRules(ns)
    for ns in nsrsbhs:
        listall.append(getTestCaseMessage(ns)[0])
    forExcel.getExcel(listall)