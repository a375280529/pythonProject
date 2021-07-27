#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyclass import conOracle,forExcel

if __name__ == '__main__':
    ff=forExcel.readExcelSheet("D:\\1231231.xlsx")
    map1={}
    list1=[]
    list2=[]
    for a in ff[0]:
        ii="a"
        i=0
        map2={}
        for b in a.keys():
            i+=1
            ii+=str(i)
            if b=="NSRSBH":
                map2[ii]=a[b]
            elif b=="SQSJ":
                map2[ii]=a[b]
            else:
                map2[ii]=b+"="+a[b]
        list2.append(map2)
    map1["shuju"]=list2
    list1.append(map1)
    print(list1)
    forExcel.getExcel(list1)