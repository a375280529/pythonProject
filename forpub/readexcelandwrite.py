#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyclass import conOracle,forExcel

if __name__ == '__main__':
    ff=forExcel.readExcelSheet("C:\\Users\\zhangc\\Desktop\\vzbzkuyongli\\成都银行测试用例-2022-04-19-01.xlsx")
    map1={}
    list1=[]
    list2=[]
    for a in ff[0]:
        i=0
        map2={}
        for b in a.keys():
            # if b!="NSRSBH" and b!="SPSJ" and b!='SW_SBZS_ZNJCS_12M_ZZSSDS' and b!='SW_SB_SFLHY_A' and b!='SW_SB_SCSB' and b!='SW_SBZS_YCJNCS_03M_ZZSSDS' and b!='SW_SB_NSZE_ZZSQYSDS_12M' and b!='SW_SB_NSZEZZL_ZZSQYSDS_12M_A' and b!='SW_SB_QBXSE_12M' and b!='SW_SB_QBXSEHBZZL_03M_A' and b!='SW_SB_QBXSEZZL_06M_A' and b!='SW_SB_QBXSEZZL_12M_A' and b!='SW_SB_ZDLXSB0_24M' and b!='SW_SB_LJSB0_24M' and b!='SW_LXR_FRNL' and b!='SW_SB_LJSB0_06M_Y' and b!='SW_CWBB_YYLRZCHJ_Y' and b!='SW_SB_QBXSEZZL_06M_Y' and b!='SW_CWBB_DQJKZCHJ_Y' and b!='SW_SBZS_YCJNCS_12M_M' and b!='SW_SBZS_SFLHYPLD_06M' and b!='SW_SBZS_PJTQJNTS_ZZS_06M' and b!='SW_SBZS_NSZE_ZZL_ZZS_12M_Y' and b!='SW_CWBB_JYYZB_ZZL_Y' and b!='SW_BG_JYDZ_06M' and b!='SW_SB_QBXSEHYPLD_06M' and b!='SW_SB_PJTQSBTS_ZZS_12M' and b!='SW_SBZS_YCJNCS_06M_M' and b!='SW_SBZS_SFL_ZZS_12M_Y' and b!='SW_CWBB_SYZQY_ZZL_Y' and b!='SW_CWBB_HBZJZCHJ_Y' and b!='SW_SB_LSXS_12M_M' and b!='SW_SB_SB0_JJYFS_01Q' and b!='SW_JCXX_NSRZTDM' and b!='SW_SB_LJSB0_12M' and b!='SW_SB_ZDLXSB0_12M' and b!='SW_SBZS_ZNJCS_06M_ZZSSDS' and b!='SW_JCXX_NSRXYPJ' and b!='SW_SBZS_SSFK_12M' and b!='SW_JCXX_NSRLXDM' and b!='SW_SBZS_QS' and b!='SW_SB_YQWSB' and b!='SW_SB_SFL_ZZSQYSDS_12M_A' and b!='SW_SB_QBXSEHBZZL_06M_A' and b!='SW_SBZS_ZNJCS_24M_ZZSSDS' and b!='SW_SBZS_XWFKCS_24M' and b!='SW_JCXX_YYDZ' and b!='SW_CWBB_KSYFZB' and b!='SW_CWBB_ZYYWCBZYYWSRB' and b!='SW_CWBB_ZYYWSRFYL' and b!='SW_CWBB_QMCHDQLJSRB' and b!='SW_SB_SCQB_02Q' and b!='SW_SB_SFBDL' and b!='SW_SB_LJSB0_YNSE' and b!='SW_SBZS_YCJNCS_01M_ZZSSDS' and b!='SW_JCCX_12M' and b!='SW_JCCX_06M' and b!='SW_JCCX_03M' and b!='SW_SBZS_YJQQS_1000' and b!='SW_SB_NSZE_ZZS_13_24M' and b!='SW_SB_NSZE_QYSDS_13_24M' and b!='SW_SB_NJNSZE' and b!='SW_SB_LJ0SBZB_24M' and b!='SW_SB_YNSE_6B24M' and b!='SW_SB_ZZS_QYSDS_CYL' and b!='SW_SB_QYSDS_12M' and b!='SW_SB_QYSDS_24M' and b!='SW_CWBB_YSZKZB' and b!='SW_CWBB_SDSGXLHYPLD' and b!='SW_CWBB_ZYYWSRBDLHYPLD':
            #     continue
            ii = "a"
            i+=1
            ii+=str(i)
            if b=="NSRSBH":
                map2[ii]=a[b]
            elif b=="SPSJ":
                map2[ii]=a[b]
            # elif b=="SW_SB_QBXSEZZL_03M" or b=="SW_SB_LSXS_12M" or b=="SW_SB_LJSB0_03Q" or b=="SW_SBZS_YCJNCS_12M_ZZSSDS" or b=="SW_CWBB_LDFZYYSR_QJ" or b=="SW_CWBB_JLRSYZQY_QJ" or b=="SW_WFWZ_06M" or b=="SW_LXR_FRNL":
            #     map2[ii]=b+"="+a[b]
            elif b=="NSRMC":
                sql = "select NSRSBH from zx_nsrjcxx where nsrmc='%s'" % (a[b])
                res = conOracle.queryOracleReturnMap("dev_vzbz/dev_vzbz@192.168.85.81:1521/emserver", sql)
                if res=={}:
                    sql1 = "select NSRSBH from zx_lxrxx where nsrmc='%s'" % (a[b])
                    res1 = conOracle.queryOracleReturnMap("dev_vzbz/dev_vzbz@192.168.85.81:1521/emserver", sql1)
                    if res1=={}:
                        sql2 = "select req_hm as nsrsbh from fahai_sifa_ajlc where req_mc='%s'" % (a[b])
                        res2 = conOracle.queryOracleReturnMap("dev_vzbz/dev_vzbz@192.168.85.81:1521/emserver", sql2)
                        if res2=={}:
                            print(sql2)
                            print(a[b])
                            print(123)
                            continue
                try:
                    map2[ii]=res["NSRSBH"]
                except:
                    try:
                        map2[ii] = res1["NSRSBH"]
                    except:
                        map2[ii] = res2["NSRSBH"]
            elif b=="CERTNO":
                sql3 = "select NSRSBH from zx_lxrxx where dbr_zjhm='%s'" % (a[b])
                # print(sql)
                res3 = conOracle.queryOracleReturnMap("dev_vzbz/dev_vzbz@192.168.85.81:1521/emserver", sql3)
                # print(res)
                if res3 == {}:
                    print(sql3)
                    print(a[b])
                    print(123)
                    continue
                map2[ii]=res3["NSRSBH"]
            else:
                map2[ii]=b.upper()+"="+a[b]
        list2.append(map2)
    map1["shuju"]=list2
    list1.append(map1)
    print(list1)
    forExcel.getExcel(list1)