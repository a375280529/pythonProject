#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
import os
import sys

import jsonpath
import requests as res
from bs4 import BeautifulSoup
from pyclass import forExcel as fe


if __name__ == '__main__':
    url="http://www.100ppi.com/mprice/plist-1-300-1.html"
    ff=res.get(url)
    soup = BeautifulSoup(ff.text, 'lxml')
    data = soup.select('table.lp-table.mb15')
    #print(data)
    lista=[]
    listb=[]
    list1=[]
    dd=""
    for da in data:
        bb=da.select('tr')
        i=0
        for t in bb:
            if i==0:
                th=t.select('th')
                for ah in th:
                    lista.append(ah.text)
            else:
                print(i)
                td=t.select('td')
                list1.append(str(td[0].find('a').text).strip())
                dd=str(td[0].find('a').text).strip()
                list1.append(str(td[1].find('div').text).strip())
                list1.append(str(td[2].text).strip())
                list1.append(str(td[3].text).strip())
                list1.append(str(td[4].text).strip())
                list1.append(str(td[5].text).strip())
                try:
                    list1.append(str(td[6].find('div').find('a').text).strip())
                except:
                    list1.append(str(td[6].find('div').text).strip())
                list1.append(str(td[7].text).strip())
            if i != 0:
                listb.append(list1)
                list1 = []
            i+=1
        print(list1)
    print(lista)
    print(listb)
    listza=[]
    mapza={}
    listzb=[]
    for lb in listb:
        mapzb = {}
        for ii in range(len(lb)):
            mapzb[lista[ii]]=lb[ii]
        listzb.append(mapzb)
    mapza[dd]=listzb
    listza.append(mapza)
    print(listza)
    fe.getExcel(listza)

    #print(data)
    # url = 'http://www.cntour.cn/'
    # strhtml = re.get(url)
    # soup = BeautifulSoup(strhtml.text, 'lxml')
    # #"#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li:nth-child(2) > a"
    # data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li:nth-child(2)>a')
    # print(data)

