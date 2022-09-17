#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyclass import conOracle,forExcel
from tqdm import tqdm

#去除小数点末尾的0，val为str
def quzero(val):
    try:
        #dex=val.index('.')
        listv=val.split('.')
        lista=[]
        listb=[]
        biaoshi=0
        value=listv[0]
        ot=""
        for i in listv[1]:
            lista.append(i)
        for b in reversed(lista):
            if biaoshi==0:
                if b!="0":
                    listb.append(b)
                    biaoshi=1
                else:
                    pass
            else:
                listb.append(b)
        for c in reversed(listb):
            ot+=c
        if ot=="":
            pass
        else:
            value+="."+ot
        return value
    except:
        return val

if __name__ == '__main__':
    ff=forExcel.readExcelSheet("C:\\Users\\zhangc\\Desktop\\最新vzbz税务指标结果\\gssf_t_hsj-20220506.xlsx")
    map1={}
    list1=[]
    list2=[]
    le=0
    zxc= len(ff[0])
    for a in tqdm(ff[0]):
        le+=1
        i=0
        map2={}
        for b in a.keys():
            # if b!="NSRSBH" and b!="SPSJ" and b!='GS_TZBL_FR' and b!='GS_BGCS_FR_6M' and b!='GS_BGCS_FR_1Y' and b!='GS_BGCS_FR_2Y' and b!='GS_BGCS_FR_3Y' and b!='GS_BGCS_FR_5Y' and b!='GS_BGSC_FR' and b!='GS_YYZT' and b!='GS_BGSC_QYMC_2Y' and b!='GS_BGCS_ZCDZ_2Y' and b!='GS_BGSC_QYMC_1Y' and b!='GS_BGSC_QYMC_3Y' and b!='GS_BGSC_QYMC_5Y' and b!='GS_BGCS_ZCDZ_1Y' and b!='GS_BGCS_ZCDZ_3Y' and b!='GS_BGCS_ZCDZ_5Y' and b!='GS_BGCS_GD_1Y' and b!='GS_BGCS_GD_2Y' and b!='GS_BGCS_GD_3Y' and b!='GS_BGCS_GD_5Y' and b!='SF_HSJ_ZDFLSS_BG_1Y_QY' and b!='SF_HSJ_ZDFLSS_BG_2Y_QY' and b!='SF_HSJ_ZDFLSS_BG_3Y_QY' and b!='SF_HSJ_ZDFLSS_BG_5Y_QY' and b!='SF_HSJ_FLDJF_BG_1Y_QY' and b!='SF_HSJ_FLDJF_BG_2Y_QY' and b!='SF_HSJ_FLDJF_BG_3Y_QY' and b!='SF_HSJ_FLDJF_BG_5Y_QY' and b!='SF_HSJ_GDZMTZGS_QY' and b!='SF_HSJ_FRCGSC_QY':
            #     continue
            ii = "a"
            i+=1
            ii+=str(i)
            if b=="NSRSBH":
                map2[ii]=a[b]
            elif b=="ID":
                continue
            elif b=="SPSJ" or b=="SP_SJ":
                map2[ii]=a[b]
            elif b=="NSRMC":
                map2[ii]=a[b]
            elif b=="CERTNO":
                map2[ii]=a[b]
            # elif b=="SW_SB_QBXSEZZL_03M" or b=="SW_SB_LSXS_12M" or b=="SW_SB_LJSB0_03Q" or b=="SW_SBZS_YCJNCS_12M_ZZSSDS" or b=="SW_CWBB_LDFZYYSR_QJ" or b=="SW_CWBB_JLRSYZQY_QJ" or b=="SW_WFWZ_06M" or b=="SW_LXR_FRNL":
            #     map2[ii]=b+"="+a[b]
            # elif b=="NSRMC":
            #     sql = "select NSRSBH from zx_nsrjcxx where nsrmc='%s'" % (a[b])
            #     res = conOracle.queryOracleReturnMap("dev_vzbz/dev_vzbz@192.168.85.81:1521/emserver", sql)
            #     if res=={}:
            #         sql1 = "select NSRSBH from zx_lxrxx where nsrmc='%s'" % (a[b])
            #         res1 = conOracle.queryOracleReturnMap("dev_vzbz/dev_vzbz@192.168.85.81:1521/emserver", sql1)
            #         if res1=={}:
            #             sql2 = "select req_hm as nsrsbh from fahai_sifa_ajlc where req_mc='%s'" % (a[b])
            #             res2 = conOracle.queryOracleReturnMap("dev_vzbz/dev_vzbz@192.168.85.81:1521/emserver", sql2)
            #             if res2=={}:
            #                 print(sql2)
            #                 print(a[b])
            #                 print(123)
            #                 continue
            #     try:
            #         map2[ii]=res["NSRSBH"]
            #     except:
            #         try:
            #             map2[ii] = res1["NSRSBH"]
            #         except:
            #             map2[ii] = res2["NSRSBH"]
            # elif b=="CERTNO":
            #     sql3 = "select NSRSBH from zx_lxrxx where dbr_zjhm='%s'" % (a[b])
            #     # print(sql)
            #     res3 = conOracle.queryOracleReturnMap("dev_vzbz/dev_vzbz@192.168.85.81:1521/emserver", sql3)
            #     # print(res)
            #     if res3 == {}:
            #         print(sql3)
            #         print(a[b])
            #         print(123)
            #         continue
            #     map2[ii]=res3["NSRSBH"]
            else:
                map2[ii]=b.upper()+"="+a[b]
        list2.append(map2)
        if zxc==le:
            map1["shuju"] = list2
            list1.append(map1)
            # print(list1)
            forExcel.getExcel(list1)
    # map1["shuju"]=list2
    # list1.append(map1)
    # #print(list1)
    # forExcel.getExcel(list1)