#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyclass import conOracle,forExcel

if __name__ == '__main__':
    ff=forExcel.readExcelSheet("D:\\zxc.xlsx")
    map1={}
    list1=[]
    list2=[]
    for a in ff[0]:
        i=0
        map2={}
        for b in a.keys():
            ii = "a"
            i+=1
            ii+=str(i)
            if b=="NSRSBH":
                map2[ii]=a[b]
            elif b=="SPSJ":
                map2[ii]=a[b]
            elif b=="SW_SB_QBXSEZZL_03M" or b=="SW_SB_LSXS_12M" or b=="SW_SB_LJSB0_03Q" or b=="SW_SBZS_YCJNCS_12M_ZZSSDS" or b=="SW_CWBB_LDFZYYSR_QJ" or b=="SW_CWBB_JLRSYZQY_QJ" or b=="SW_WFWZ_06M" or b=="SW_LXR_FRNL":
                map2[ii]=b+"="+a[b]
            else:
                pass
        list2.append(map2)
    map1["shuju"]=list2
    list1.append(map1)
    print(list1)
    forExcel.getExcel(list1)