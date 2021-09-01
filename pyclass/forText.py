#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
from forpub import forFinal

def writeTxt(txt):
    img_path = forFinal.getIni("logger.ini")["model"]["savetxtpath"] + time.strftime("%Y%m%d",time.localtime())
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    excelpath = img_path + "\\result"+ time.strftime("%Y%m%d%H%M%S",time.localtime())+".txt"
    with open(excelpath, "a+", encoding="utf-8") as f:
        f.writelines(txt)

def readTxt(url):
    with open(url, "r", encoding="utf-8") as f:
        txt=f.readlines()
        return txt

if __name__ == '__main__':
    dd=readTxt("F:\\z\\1.txt")
    va1=""
    va2=""
    va3=""
    map2={}
    list1=[]
    list2=[]
    map22 = {}
    list11 = []
    list22 = []
    print(len(dd))
    i=0
    a=0
    b=0
    for va in dd:
        i+=1
        # map1={}
        # map11 = {}
        kk=va.split("|")
        if kk[1][0:4] =="9142":
            va1+=va
            # map1["名称"]=kk[0]
            # map1["税号"]=kk[1]
        elif kk[1][0:4] =="9242":
            va1+=va
            # map1["名称"] = kk[0]
            # map1["税号"] = kk[1]
        elif kk[1][0:4] == "9342":
            va1+=va
            # map1["名称"] = kk[0]
            # map1["税号"] = kk[1]
        elif kk[1][0:2] == "42":
            va1+=va
            # map1["名称"] = kk[0]
            # map1["税号"] = kk[1]
        elif kk[1][0:4] == "9161":
            va2+=va
            # map1["名称"] = kk[0]
            # map1["税号"] = kk[1]
        elif kk[1][0:4] == "9261":
            va2+=va
            # map1["名称"] = kk[0]
            # map1["税号"] = kk[1]
        elif kk[1][0:4] == "9361":
            va2+=va
            # map1["名称"] = kk[0]
            # map1["税号"] = kk[1]
        elif kk[1][0:2] == "61":
            va2+=va
            # map1["名称"] = kk[0]
            # map1["税号"] = kk[1]
        else:
            va3+=va
            # map11["名称"] = kk[0]
            # map11["税号"] = kk[1]
        # if map1!={}:
        #     list1.append(map1)
        # if map11!={}:
        #     list11.append(map11)
        # if len(list1)==1000000:
        #     map2["数据"+str(a)] = list1
        #     list1=[]
        #     list2.append(map2)
        #     map2={}
        #     a+=1
        # if len(list11)==1000000:
        #     map22["数据"+str(b)] = list11
        #     list11=[]
        #     list22.append(map22)
        #     map22={}
        #     b+=1
        if i%333333==0:
            print(i)
        if i%999999==0:
            writeTxt(va1)
            time.sleep(1)
            writeTxt(va2)
            time.sleep(1)
            writeTxt(va3)
            time.sleep(1)
            va1=""
            va2=""
            va3 = ""
        elif i%7094092==0:
            writeTxt(va1)
            time.sleep(1)
            writeTxt(va2)
            time.sleep(1)
            writeTxt(va3)
            time.sleep(1)
            va1 = ""
            va2 = ""
            va3 = ""
    # if list1!=[]:
    #     map2["数据"+str(a)] = list1
    #     list2.append(map2)
    # if list11!=[]:
    #     map22["数据" + str(b)] = list11
    #     list22.append(map22)
    # print(list2)
    # print(list22)

    # writeTxt(va1)
    # time.sleep(1)
    # writeTxt(va2)
    # time.sleep(1)
    # forExcel.getExcel(list2)
    # time.sleep(1)
    # forExcel.getExcel(list22)