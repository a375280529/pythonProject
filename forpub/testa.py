#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
import os
import sys
import traceback
import turtle
import jsonpath
import requests
import pandas as pd
from pyclass import forExcel as fe
import re
from ctypes import *
import forFinal
from pyclass import forText as ft

def getStr(alllist,array,retStr,j,indexId):
    id=j["id"]
    if array!=[]:
        index=0
        for json in array:
            child=json["child"]
            ids=json["id"]
            if id == ids:
                retStr += "@@@@@@" + json["name"]
                indexId += "@@@@@@" + json["child"]
            else:
                if id in child:
                    retStr += "@@@@@@" + j["name"]
                    indexId += "@@@@@@" + j["child"]
                    index+=1
                    break
        if index!=0:
            getStr(alllist,array, retStr, json, indexId)
            return
        if indexId.split("@@@@@@")[1]=="":
            alllist.append(retStr)

def quzero(val):
    try:
        dex=val.index('.')
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
    bb = '1.01001'
    zx = quzero(bb)
    print(zx)

    # json = "...";
    # List < String > authors = JsonPath.read(json, "$.store.book[*].author");
    dd='{"aa":"bb","cc":"dd"}'
    ff=json.loads(dd)
    print(jsonpath.jsonpath(ff,"$..aa"))

    d = {
        "error_code": 0,
        "stu_info": [
            {
                "id": 2059,
                "name": "小白",
                "sex": "男",
                "age": 28,
                "addr": "河南省济源市北海大道32号",
                "grade": "天蝎座",
                "phone": "18378309272",
                "gold": 10896,
                "info": {
                    "card": 434345432,
                    "bank_name": '中国银行'
                }

            },
            {
                "id": 2067,
                "name": "小黑",
                "sex": "男",
                "age": 28,
                "addr": "河南省济源市北海大道32号",
                "grade": "天蝎座",
                "phone": "12345678915",
                "gold": 100
            }
            ,
            {
                "id": 2068,
                "name": "小11",
                "sex": "男",
                "age": 28,
                "addr": "河南省济源市北海大道32号",
                "grade": "天蝎座",
                "phone": "16665678915",
                "gold": 100
            }
        ]
    }
    import jsonpath

    fff={'nodesInfo': [{'name': '输入', 'id': 0, 'type': 'INPUT', 'rulesInfo': [], 'modelInfo': None, 'scoreCardInfo': None, 'actionInfo': None, 'output': None, 'dtableInfo': None}, {'name': '转换节点', 'id': 1, 'type': 'NODE', 'rulesInfo': [], 'modelInfo': None, 'scoreCardInfo': None, 'actionInfo': None, 'output': None, 'dtableInfo': None}, {'name': '个体户', 'id': 2, 'type': 'DECISION', 'rulesInfo': [{'code': 'R_17896_00112', 'name': '通用强规则-申报表缺失', 'description': '', 'version': 2, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00113', 'name': '一般强规则-征收表缺失', 'description': '', 'version': 3, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00114', 'name': '通用强规则-年龄', 'description': '强规则-年龄', 'version': 3, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00115', 'name': '通用强规则-经营年限', 'description': '强规则-经营年限', 'version': 3, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00117', 'name': '通用强规则-纳税信用评级', 'description': '', 'version': 2, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00118', 'name': '通用强规则-最近一期是否按时申报', 'description': '', 'version': 2, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00119', 'name': '通用强规则-近24个月重大涉税违法情况', 'description': '', 'version': 2, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00120', 'name': '通用强规则-当前有无欠税行为', 'description': '', 'version': 2, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00121', 'name': '通用强规则-近12个月滞纳金产生次数', 'description': '', 'version': 2, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00122', 'name': '通用强规则-近6个月滞纳金产生次数', 'description': '', 'version': 1, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00123', 'name': '通用强规则-行为涉税违法总次数', 'description': '', 'version': 1, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00124', 'name': '通用强规则-涉税罚款情况', 'description': '', 'version': 1, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00144', 'name': '通用强规则-缴税延迟情况', 'description': '', 'version': 2, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00162', 'name': '通用强规则-纳税状态', 'description': '', 'version': 4, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00164', 'name': '行业黑名单', 'description': '', 'version': 1, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00132', 'name': '通用-弱规则-最近2期的全部销售收入加总金额<=0', 'description': '', 'version': 2, 'value': True, 'hit': True, 'point': 1.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00127', 'name': '小规模/个体-弱规则-近3个月环比<=-0.5且近6个月同比<=-0.4', 'description': '', 'version': 1, 'value': True, 'hit': True, 'point': 1.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00135', 'name': '个体-弱规则-近12个月的全部销售收入小于12万元', 'description': '', 'version': 1, 'value': True, 'hit': True, 'point': 1.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00138', 'name': '个体-弱规则-近3个月全部销售额占比近12个月销售额90%以上', 'description': '', 'version': 1, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00134', 'name': '小规模/个体-弱规则-近12个月增值税应纳税额小于1000元', 'description': '', 'version': 2, 'value': True, 'hit': True, 'point': 1.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00146', 'name': '通用弱规则-近3个月全部销售额占比近12个月销售额90%以上', 'description': '', 'version': 2, 'value': False, 'hit': False, 'point': 0.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00126', 'name': '通用弱规则-首次有收入报税时间<13个月', 'description': '', 'version': 1, 'value': True, 'hit': True, 'point': 1.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00128', 'name': '小规模/个体-弱规则-近12个月同比<=-0.5', 'description': '', 'version': 1, 'value': True, 'hit': True, 'point': 1.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00161', 'name': '个人-弱规则-个体户非本地户籍与企业注册地不匹配', 'description': '', 'version': 2, 'value': True, 'hit': True, 'point': 1.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}, {'code': 'R_17896_00145', 'name': '小规模/个体-弱规则-近12个月增值税报税收入为0的次数最大累计次数>=2', 'description': '', 'version': 2, 'value': True, 'hit': True, 'point': 1.0, 'tsdbError': False, 'state': 'ENABLE', 'decisionCode': '', 'decisionCodePriority': -1}], 'modelInfo': None, 'scoreCardInfo': None, 'actionInfo': None, 'output': 8.0, 'dtableInfo': None}, {'name': '终止节点', 'id': 5, 'type': 'FINAL', 'rulesInfo': [], 'modelInfo': None, 'scoreCardInfo': None, 'actionInfo': None, 'output': None, 'dtableInfo': None}, {'name': '转换节点', 'id': 11, 'type': 'NODE', 'rulesInfo': [], 'modelInfo': None, 'scoreCardInfo': None, 'actionInfo': None, 'output': None, 'dtableInfo': None}]}
    print(123123123123123123)
    zxcvbn=jsonpath.jsonpath(fff, '$..rulesInfo[?(@.hit==True)].name')
    print(';'.join(zxcvbn))
    tlist = ['1']
    print(''.join(tlist))
    res = d["stu_info"][1]['name']  # 取某个学生姓名的原始方法:通过查找字典中的key以及list方法中的下标索引
    print(res)  # 输出结果是：小黑


    res1 = jsonpath.jsonpath(d, '$..name')  # 嵌套n层也能取到所有学生姓名信息,$表示最外层的{}，..表示模糊匹配
    print(res1)  # 输出结果是list：['小白', '小黑']

    res2 = jsonpath.jsonpath(d, '$..bank_name')
    print(res2)  # 输出结果是list：['中国银行']

    res3 = jsonpath.jsonpath(d, '$..name123')  # 当传入不存在的key(name)时,返回False
    print(res3)  # 输出结果是：False

    print(jsonpath.jsonpath(d,'$.rulesInfo[?(@.phone=="16665678915")].name'))

    # aa='<?xml version="1.0"?><Page ID="100" Type="Page" Name="页面-1" Zoom="1" QuickMask="0"><PageProps><Width V="3504"/><Height V="1620"/><CX V="1152" B="1" P="0"/><CY V="810" B="2" P="0"/><ScrollX V="0.641342"/><ScrollY V="0.389027"/></PageProps><Layout><HSpacing V="30"/><VSpacing V="17"/><Layout V="8"/><SectorAlign V="1"/></Layout><FillFormat/><PrintSetup FittoSheet="1" HSheet="1" VSheet="1" Background="1" Width="210" Height="297" Unit="mm" LeftMargin="10" TopMargin="10" RightMargin="10" BottomMargin="10"/><Theme ID="40" Rainbow="0" Effect="0" Name="Edraw"><ThemeColor V="3"/><ThemeEffect V="40"/><ThemeText V="40"/><ThemeShape V="40"/></Theme><Shape ID="415" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="1264.78" B="1" P="0"/><CY V="810" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="3"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="101"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="49.78" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><CurveTo><X V="112.78" B="1" P="0"/><Y V="0" B="2" P="0"/><A V="65.6499" B="1" P="0"/><B V="0" B="2" P="0"/><C V="87.253" B="1" P="0"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="1152" Y="810"/><EndPt X="1377.56" Y="810"/><MMConnector FlexoStyle="5" Thickness="0"/></Shape><Shape ID="417" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="1641.36" B="1" P="0"/><CY V="766.975" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="2982"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-21.6" B="1" P="0"/><Y V="43.025" B="2" P="0"/></MoveTo><LineTo><X V="-10.6" B="1" P="0"/><Y V="43.025" B="2" P="0"/></LineTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="-43.025" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="-43.025" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="-43.025" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="1619.76" Y="810"/><EndPt X="1662.96" Y="723.95"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="418" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="1641.36" B="1" P="0"/><CY V="819.5" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="2982"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-10.6" B="1" P="0"/><Y V="-9.5" B="2" P="0"/></MoveTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="9.5" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="9.5" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="9.5" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="1619.76" Y="810"/><EndPt X="1662.96" Y="829"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="419" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="1641.36" B="1" P="0"/><CY V="853.025" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="2982"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-10.6" B="1" P="0"/><Y V="-43.025" B="2" P="0"/></MoveTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="43.025" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="43.025" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="43.025" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="1619.76" Y="810"/><EndPt X="1662.96" Y="896.05"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="420" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="2164.76" B="1" P="0"/><CY V="723.95" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="454"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-21.6" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="-10.6" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="0" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="0" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="2143.16" Y="723.95"/><EndPt X="2186.36" Y="723.95"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="421" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="1754.56" B="1" P="0"/><CY V="723.95" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="450"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-21.6" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="-10.6" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="0" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="0" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="1732.96" Y="723.95"/><EndPt X="1776.16" Y="723.95"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="422" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="1754.56" B="1" P="0"/><CY V="829" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="451"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-21.6" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="-10.6" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="0" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="0" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="1732.96" Y="829"/><EndPt X="1776.16" Y="829"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="423" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="2164.76" B="1" P="0"/><CY V="829" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="455"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-21.6" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="-10.6" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="0" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="0" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="2143.16" Y="829"/><EndPt X="2186.36" Y="829"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="424" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="1760.56" B="1" P="0"/><CY V="896.05" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="452"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-21.6" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="-10.6" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="0" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="0" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="1738.96" Y="896.05"/><EndPt X="1782.16" Y="896.05"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="425" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="2170.76" B="1" P="0"/><CY V="896.05" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="457"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-21.6" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="-10.6" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="0" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="0" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="2149.16" Y="896.05"/><EndPt X="2192.36" Y="896.05"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="2984" Type="MMConnector"><Transform><Width V="0"/><Height V="0"/><CX V="1522.16" B="1" P="0"/><CY V="810" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat/><LineFormat><LineWeight V="1"/><Rounding V="3"/><LineCap V="Round"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><LevelData><Super V="448"/></LevelData><Geometries><Geometry Closed="0"><MoveTo><X V="-21.6" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="-10.6" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo><CurveTo><X V="21.6" B="1" P="0"/><Y V="0" B="2" P="0"/><A V="5.672" B="1" P="0"/><B V="0" B="2" P="0"/><C V="5.672" B="1" P="0"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="1"/><BeginPt X="1500.56" Y="810"/><EndPt X="1543.76" Y="810"/><MMConnector FlexoStyle="11" Thickness="0"/></Shape><Shape ID="101" Type="MainIdea"><Transform><Width V="325.12"/><Height V="63"/><CX V="1152" B="1" P="0"/><CY V="810" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color ThemeColor="10" V="#ff00af54"/></FillFormat><LineFormat><LineWeight V="3"/><LineFill Type="Solid"><Color ThemeColor="10" V="#ff00af54"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="274"/><Height V="31"/><CX V="162.86" B="1" P="0"/><CY V="30.95" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="1" V="#ffffffff"/><Character IX="0" Family="微软雅黑" Size="18" Style="1" Color="#ffffff"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">极速猎豹-两融-算法交易-</tp></pp></Text></TextBlock></Text><LevelData><SubLevel V="448"/></LevelData><Geometries><Geometry Closed="1"><MoveTo><X V="31.5" B="5" P="0.5"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="293.62" B="6" P="0.5"/><Y V="0" B="2" P="0"/></LineTo><CurveTo><X V="325.12" B="1" P="1"/><Y V="31.5" B="2" P="0.5"/><A V="311.017" B="6" P="0.22385"/><B V="0" B="2" P="0"/><C V="325.12" B="1" P="1"/><D V="14.1025" B="5" P="0.22385"/></CurveTo><CurveTo><X V="293.62" B="6" P="0.5"/><Y V="63" B="2" P="1"/><A V="325.12" B="1" P="1"/><B V="48.8974" B="7" P="0.22385"/><C V="311.017" B="6" P="0.22385"/><D V="63" B="2" P="1"/></CurveTo><LineTo><X V="31.5" B="5" P="0.5"/><Y V="63" B="2" P="1"/></LineTo><CurveTo><X V="0" B="1" P="0"/><Y V="31.5" B="2" P="0.5"/><A V="14.1025" B="5" P="0.22385"/><B V="63" B="2" P="1"/><C V="0" B="1" P="0"/><D V="48.8974" B="7" P="0.22385"/></CurveTo><CurveTo><X V="31.5" B="5" P="0.5"/><Y V="0" B="2" P="0"/><A V="0" B="1" P="0"/><B V="14.1025" B="5" P="0.22385"/><C V="14.1025" B="5" P="0.22385"/><D V="0" B="2" P="0"/></CurveTo></Geometry></Geometries><ShapeStyle V="11"/><Layout><ImagePos V="0"/><FlexoStyle V="5"/><Layout V="8"/><Margins LeftMargin="18" TopMargin="14" RightMargin="18" BottomMargin="14"/></Layout></Shape><Shape ID="448" Type="MainTopic"><Transform><Width V="123"/><Height V="43"/><CX V="1439.06" B="1" P="0"/><CY V="810" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="2"/><Rounding V="4"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="88"/><Height V="26"/><CX V="61.8" B="1" P="0"/><CY V="20.95" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="14" Style="1" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">界面检查-</tp></pp></Text></TextBlock></Text><LevelData><Super V="101"/><ToSuper V="415"/><SubLevel V="2982"/></LevelData><Geometries><Geometry Closed="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="123" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="123" B="1" P="1"/><Y V="43" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="43" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry></Geometries><ShapeStyle V="1"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="16" TopMargin="7" RightMargin="16" BottomMargin="7"/></Layout></Shape><Shape ID="450" Type="SubTopic"><Transform><Width V="70"/><Height V="24.5"/><CX V="1697.96" B="1" P="0"/><CY V="711.7" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="56"/><Height V="19"/><CX V="35" B="1" P="0"/><CY V="11.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">算法母单</tp></pp></Text></TextBlock></Text><LevelData><Super V="2982"/><ToSuper V="417"/><SubLevel V="454"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="70" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="70" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></MoveTo><LineTo><X V="70" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="451" Type="SubTopic"><Transform><Width V="70"/><Height V="24.5"/><CX V="1697.96" B="1" P="0"/><CY V="816.75" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="56"/><Height V="19"/><CX V="35" B="1" P="0"/><CY V="11.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">算法子单</tp></pp></Text></TextBlock></Text><LevelData><Super V="2982"/><ToSuper V="418"/><SubLevel V="455"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="70" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="70" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></MoveTo><LineTo><X V="70" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="452" Type="SubTopic"><Transform><Width V="76"/><Height V="24.5"/><CX V="1700.96" B="1" P="0"/><CY V="883.8" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="62"/><Height V="19"/><CX V="38" B="1" P="0"/><CY V="11.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">日志监控-</tp></pp></Text></TextBlock></Text><LevelData><Super V="2982"/><ToSuper V="419"/><SubLevel V="457"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="76" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="76" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></MoveTo><LineTo><X V="76" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="453" Type="SubTopic"><Transform><Width V="514"/><Height V="157.5"/><CX V="2443.36" B="1" P="0"/><CY V="645.2" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="500"/><Height V="152"/><CX V="257" B="1" P="0"/><CY V="78.1" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">1.按钮：新建算法、导入算法、批量停止、批量继续、批量关闭、导出订单，按需求格式展示正确。</tp></pp><pp PX="0" CX="0"><tp CX="0">2.下拉框：全部母单-‘全部母单’‘组合号码’；全部状态-‘全部状态’‘待启动’‘运行中’‘已停止’‘已完成’；全部算法-‘全部算法’‘TWAP’‘VWAP’‘VP’</tp></pp><pp PX="0" CX="0"><tp CX="0">3.字段：状态、证券代码、证券名称、交易方向、完成度、目标量、成交量、成交全额、成交均价、母单ID、开始时间、完成时间、母单信息，按顺序展示以上字段，点击字段名可正确升降序排列，每个字段可拖拽拉宽显示栏。</tp></pp></Text></TextBlock></Text><LevelData><Super V="454"/><ToSuper V="420"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="514" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="514" B="1" P="1"/><Y V="157.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="157.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="157.5" B="2" P="1"/></MoveTo><LineTo><X V="514" B="1" P="1"/><Y V="157.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="454" Type="SubTopic"><Transform><Width V="367"/><Height V="24.5"/><CX V="1959.66" B="1" P="0"/><CY V="711.7" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="353"/><Height V="19"/><CX V="183.5" B="1" P="0"/><CY V="11.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">1.登录账号，点击策略栏，进入算法交易界面，检查界面展示</tp></pp></Text></TextBlock></Text><LevelData><Super V="450"/><ToSuper V="421"/><SubLevel V="453"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="367" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="367" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></MoveTo><LineTo><X V="367" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="455" Type="SubTopic"><Transform><Width V="367"/><Height V="24.5"/><CX V="1959.66" B="1" P="0"/><CY V="816.75" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="353"/><Height V="19"/><CX V="183.5" B="1" P="0"/><CY V="11.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">1.登录账号，点击策略栏，进入算法交易界面，检查界面展示</tp></pp></Text></TextBlock></Text><LevelData><Super V="451"/><ToSuper V="422"/><SubLevel V="456"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="367" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="367" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></MoveTo><LineTo><X V="367" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="456" Type="SubTopic"><Transform><Width V="514"/><Height V="100.5"/><CX V="2443.36" B="1" P="0"/><CY V="778.75" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="500"/><Height V="95"/><CX V="257" B="1" P="0"/><CY V="49.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">1.界面显示，记录：*/*   下拉框：全部状态-‘全部状态’‘已报’‘部成’‘已成’‘部成部撤’‘全撤’‘拒绝’</tp></pp><pp PX="0" CX="0"><tp CX="0">2.字段：下单时间、代码、名称、交易方向、算法类型、状态、委托数量、委托价格、成交数量、成交价格、成交全额、订单号、错误信息，按顺序展示以上字段，点击字段名可正确升降序排列，每个字段可拖拽拉宽显示栏。</tp></pp></Text></TextBlock></Text><LevelData><Super V="455"/><ToSuper V="423"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="514" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="514" B="1" P="1"/><Y V="100.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="100.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="100.5" B="2" P="1"/></MoveTo><LineTo><X V="514" B="1" P="1"/><Y V="100.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="457" Type="SubTopic"><Transform><Width V="367"/><Height V="24.5"/><CX V="1965.66" B="1" P="0"/><CY V="883.8" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="353"/><Height V="19"/><CX V="183.5" B="1" P="0"/><CY V="11.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">1.登录账号，点击策略栏，进入算法交易界面，检查界面展示</tp></pp></Text></TextBlock></Text><LevelData><Super V="452"/><ToSuper V="424"/><SubLevel V="458"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="367" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="367" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></MoveTo><LineTo><X V="367" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="458" Type="SubTopic"><Transform><Width V="439"/><Height V="62.5"/><CX V="2411.86" B="1" P="0"/><CY V="864.8" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="425"/><Height V="57"/><CX V="219.5" B="1" P="0"/><CY V="30.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">1.下拉框：全部算法实例-‘全部算法实例’‘系统消息’‘所有母单ID’</tp></pp><pp PX="0" CX="0"><tp CX="0">2.按钮：详细日志</tp></pp><pp PX="0" CX="0"><tp CX="0">3.字段：时间、母单ID、消息内容，每个字段可拖拽拉宽显示栏</tp></pp></Text></TextBlock></Text><LevelData><Super V="457"/><ToSuper V="425"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="439" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="439" B="1" P="1"/><Y V="62.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="62.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="62.5" B="2" P="1"/></MoveTo><LineTo><X V="439" B="1" P="1"/><Y V="62.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape><Shape ID="2982" Type="SubTopic"><Transform><Width V="76"/><Height V="24.5"/><CX V="1581.76" B="1" P="0"/><CY V="797.75" B="2" P="0"/></Transform><ShapeFormat QuickMask="0"><FillFormat Type="Solid"><Color V="#ffffffff"/></FillFormat><LineFormat><LineWeight V="1"/><LineFill Type="Solid"><Color ThemeColor="2" Tint="6" V="#ff454545" Ref="#000"/></LineFill></LineFormat></ShapeFormat><Text><Transform><Width V="62"/><Height V="19"/><CX V="38" B="1" P="0"/><CY V="11.6" B="2" P="0"/></Transform><TextBlock TextFormatMask="0"><Color ThemeColor="2" Tint="3" V="#ff303030" Ref="#000"/><Character IX="0" Family="微软雅黑" Size="10" Color="#303030"/><Paragraph IX="0" Align="1" SpLine="100"/><Text><pp PX="0" CX="0"><tp CX="0">算法交易-</tp></pp></Text></TextBlock></Text><LevelData><Super V="448"/><ToSuper V="2984"/><SubLevel V="450;451;452"/></LevelData><Geometries><Geometry Closed="1" NoLine="1"><MoveTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></MoveTo><LineTo><X V="76" B="1" P="1"/><Y V="0" B="2" P="0"/></LineTo><LineTo><X V="76" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></LineTo><LineTo><X V="0" B="1" P="0"/><Y V="0" B="2" P="0"/></LineTo></Geometry><Geometry Closed="0" NoFill="1"><MoveTo><X V="0" B="1" P="0"/><Y V="24.5" B="2" P="1"/></MoveTo><LineTo><X V="76" B="1" P="1"/><Y V="24.5" B="2" P="1"/></LineTo></Geometry></Geometries><ShapeStyle V="5"/><Layout><ImagePos V="1"/><FlexoStyle V="11"/><Layout V="6"/><Margins LeftMargin="7" TopMargin="2" RightMargin="7" BottomMargin="2"/></Layout></Shape></Page>'
    # bb=aa.split('<Shape ID="101" Type="MainIdea">')
    # cc=bb[1]
    # dd=cc.split("</Shape>")
    # array=[]
    # for i in range(len(dd)):
    #     mapa={}
    #     kk=""
    #     if i==0:
    #         pass
    #     elif i==len(dd)-1:
    #         pass
    #     else:
    #         ff=dd[i].split('<Shape ID="')
    #         gg=ff[1].split('"')
    #         hh=dd[i].split("</tp>")
    #         ii=""
    #         if len(hh)>2:
    #             for ei in range(len(hh)):
    #                 if ei==len(hh)-1:
    #                     pass
    #                 else:
    #                     ii+="\n"+hh[ei].split(">")[-1]
    #         else:
    #             ii=hh[0].split(">")[-1]
    #         jj=dd[i].split('<SubLevel V="')
    #         if len(jj)<=1:
    #             kk=""
    #         else:
    #             kk=jj[1].split('"')[0]
    #         mapa["id"] = gg[0]
    #         mapa["name"] = ii
    #         mapa["child"] = kk
    #         array.append(mapa)
    # print(array)


    # indexId=""
    # retStr=""
    # alllist=[]
    # changelist=[]
    # for json in array:
    #     getStr(alllist,array,retStr,json,indexId)
    # for zz in alllist:
    #     xx=zz.split("@@@@@@")
    #     zxc=""
    #     for zx in reversed(xx):
    #         if zx!="":
    #             zxc+="@@@@@@"+zx
    #     changelist.append(zxc)
    # print(changelist)
    #
    # mapone = {}
    # listone=[]
    # listtwo=[]
    # for ali in changelist:
    #     maptwo={"用例名称":"","用例步骤":"","用例期望":""}
    #     lista=ali.split("@@@@@@")
    #     va=""
    #     for le in range(len(lista)):
    #         if le==len(lista)-1:
    #             maptwo["用例期望"]=lista[le]
    #         elif le==len(lista)-2:
    #             maptwo["用例步骤"]=lista[le]
    #         else:
    #             va+=lista[le]+"_"
    #     maptwo["用例名称"]=va[:-1][1:]
    #     listtwo.append(maptwo)
    # mapone["测试用例"]=listtwo
    # listone.append(mapone)
    # print(listone)
    # deleteFile(filedir)
    # getExcel(listone)

    # a, b, c = tuple(map(int, input('请输入a, b, c: ').strip().split(' ')))
    # print(a, type(a), b, type(b), c, type(c))
    # dataInput = list(map(str, input('请输入dataInput: ').strip().split(',')))
    # print(dataInput)
    a = 1.0110 # 结果要求为12.123
    b = 12.00  # 结果为12
    c = 200.12000  # 结果为200.12
    d = 200.0  # 结果为200
    print(type(a))
    #a=[str(a),int(a)][int(a)==a]
    b = [str(b), int(b)][int(b) == b]
    c = [str(c), int(c)][int(c) == c]
    d = [str(d), int(d)][int(d) == d]
    print(type(a))
    print(b)
    print(c)
    print(d)

    a='{:g}'.format(a)
    print(a)

    zva=""
    j=0
    for i in range(11):
        if i==0:
            zva+="........1..............1........."+"\n"
        elif i==1:
            zva+=".....1.....1........1......1....."+"\n"
        elif i==2:
            zva+="...1.........1....1..........1..."+"\n"
        elif i==3:
            zva+="..1.............1..............1."+"\n"
        elif i==4:
            zva+="...1.........................1..."+"\n"
        elif i==5:
            zva+=".....1.....................1....."+"\n"
        elif i==6:
            zva+=".......1.................1......."+"\n"
        elif i==7:
            zva+=".........1.............1........."+"\n"
        elif i==8:
            zva+="............1........1..........."+"\n"
        elif i==9:
            zva+="..............1....1............."+"\n"
        else:
            zva += ".................1..............."

    dfa="1zxc"
    cn=dfa.upper()
    print(cn=="1ZXC")


    afd=['SW_JCXX_NSRMC,期望值：部署测试企业用104324营有限公司,实际值：None', 'SW_JCXX_CLNX,期望值：6.97,实际值：None', 'SW_JCXX_HY,期望值：5146,实际值：None', 'SW_JCXX_NSRXYPJ,期望值：B,实际值：未评级', 'SW_JCXX_NSRZTDM,期望值：3,实际值：None', 'SW_JCXX_NSRLXDM,期望值：3,实际值：None', 'SW_JCXX_DJZCLXDM,期望值：173,实际值：None', 'SW_JCXX_DJZCLXMC,期望值：私营有限责任公司,实际值：None', 'SW_JCXX_XZQH,期望值：1201,实际值：None', 'SW_LXR_FRXM,期望值：周如江,实际值：None', 'SW_LXR_FRNL,期望值：60.0,实际值：None', 'SW_LXR_FRZJHM,期望值：12010919591009**1*,实际值：None', 'SW_TZF_GQFSD,期望值：0.52,实际值：None', 'SW_JCXX_ZYRS,期望值：4.0,实际值：None', 'SW_SB_SBXX_SFQS,期望值：0,实际值：1', 'SW_SB_SSSQZ_MIN,期望值：2017-01-01,实际值：None', 'SW_SB_SSSQZ_MAX,期望值：2019-12-31,实际值：None', 'SW_SB_SCSB,期望值：39.0,实际值：None', 'SW_SB_LJSB0_24M,期望值：1,实际值：0', 'SW_SB_LSXS_12M,期望值：71.0092,实际值：None', 'SW_SB_YNSE_ZZS_12M,期望值：1824.18,实际值：0.0', 'SW_SB_ZDLXSB0_24M,期望值：1,实际值：0', 'SW_SB_QBXSE_03M,期望值：28048.54,实际值：0.0', 'SW_SB_QBXSE_06M,期望值：33174.76,实际值：0.0', 'SW_SB_QBXSE_12M,期望值：60805.81,实际值：0.0', 'SW_SB_QBXSE_24M,期望值：178551.92,实际值：0.0', 'SW_SB_NSZE_ZZSQYSDS_24M,期望值：2842.09,实际值：0.0', 'SW_SB_QBXSEZZL_06M,期望值：-0.6906,实际值：None', 'SW_SB_QBXSEZZL_12M,期望值：-0.4836,实际值：None', 'SW_SB_QBXSEZZL_06M_A,期望值：-0.6906,实际值：0.0', 'SW_SB_QBXSEZZL_12M_A,期望值：-0.4836,实际值：0.0', 'SW_SB_QBXSEHBZZL_03M_A,期望值：4.4716,实际值：0.0', 'SW_SB_QBXSEHBZZL_03M,期望值：4.4716,实际值：None', 'SW_SB_NSZEZZL_ZZSQYSDS_12M_A,期望值：-1.0,实际值：0.0', 'SW_SB_QBXSE_02Q,期望值：33174.76,实际值：0.0', 'SW_SB_YQWSB,期望值：0,实际值：1', 'SW_SB_QBXSEZZL_06M_Y,期望值：-0.6906,实际值：None', 'SW_SB_PJTQSBTS_ZZS_12M,期望值：6.0,实际值：None', 'SW_SB_LSXS_12M_M,期望值：0.7101,实际值：None', 'SW_SB_QBXSEZZL_03M_Y,期望值：-0.7039,实际值：None', 'SW_SBZS_SBZSXX_SFQS,期望值：0,实际值：1', 'SW_SBZS_NSZE_ZZSQYSDS_24M,期望值：4910.05,实际值：0.0', 'SW_SBZS_NSZE_ZZL_ZZS_12M_Y,期望值：-1.0,实际值：None', 'SW_SBZS_SFLHYPLD_06M,期望值：-1.0,实际值：None', 'SW_CWBB_SYZQY_1,期望值：994464.49,实际值：None', 'SW_CWBB_YYSR_1,期望值：117746.11,实际值：None', 'SW_CWBB_JLR_1,期望值：-1381.11,实际值：None', 'SW_CWBB_XSJLL,期望值：-0.0117,实际值：None', 'SW_CWBB_YYLRZCHJ_Y,期望值：-0.002,实际值：None', 'SW_CWBB_JYYZB_ZZL_Y,期望值：0.1241,实际值：None', 'SW_CWBB_ZZC_ZZL_Y,期望值：0.0447,实际值：None']
    print(len(afd))


    a="0.0"
    b="None"
    c="22"
    if (a!="0.0" or b!="None") and c=="22":
        print(123)

    aa=3.0
    print(int(aa))

    asdf="233353376787867.6665454562122"
    print(round(float(asdf)/1000)*1000)

    map={"aa":"123","bb":"666"}
    dd=map.get("aa")
    ff = map.get("cc",0)
    print(dd)
    print(ff)

    values="SW_JCXX_CLNX,SW_JCXX_DJZCLXDM,SW_JCXX_HY,SW_JCXX_NSRLXDM,SW_JCXX_NSRXYPJ,SW_JCXX_NSRZTDM,SW_JCXX_XZQH,SW_LXR_FRNL,SW_LXR_FRZJHM,SW_LXR_FRXM,SW_TZF_FRTZBL,SW_BG_BSRY_12M,SW_BG_CWFZR_01M,SW_BG_CWFZR_03M,SW_BG_CWFZR_06M,SW_BG_CWFZR_12M,SW_BG_CWFZR_24M,SW_BG_FR_01M,SW_BG_FR_03M,SW_BG_FR_06M,SW_BG_FR_12M,SW_BG_FR_24M,SW_BG_HY_01M,SW_BG_HY_03M,SW_BG_HY_06M,SW_BG_HY_12M,SW_BG_HY_24M,SW_BG_JYDZ_01M,SW_BG_JYDZ_03M,SW_BG_JYDZ_06M,SW_BG_JYDZ_12M,SW_BG_JYDZ_24M,SW_WFWZ_01M,SW_WFWZ_03M,SW_WFWZ_06M,SW_WFWZ_12M,SW_WFWZ_24M,SW_WFWZ_YZ_01M,SW_WFWZ_YZ_03M,SW_WFWZ_YZ_06M,SW_WFWZ_YZ_12M,SW_WFWZ_YZ_24M,SW_JCXX_NSRMC,SW_JCXX_SFZZY_A,SW_JCXX_DJZCLXMC,SW_TZF_FRTZBL_HMXM,SW_BG_FR_02M,SW_BG_FR_09M,SW_BG_FR_15M,SW_BG_FR_18M,SW_BG_FR_21M,SW_BG_HY_02M,SW_BG_HY_09M,SW_BG_HY_15M,SW_BG_HY_18M,SW_BG_HY_21M,SW_WFWZ_02M,SW_WFWZ_09M,SW_WFWZ_15M,SW_WFWZ_18M,SW_WFWZ_21M,SW_WFWZ_YZ_02M,SW_WFWZ_YZ_09M,SW_WFWZ_YZ_15M,SW_WFWZ_YZ_18M,SW_WFWZ_YZ_21M,SW_JCXX_NSRJCXX_SFQS,SW_LXR_LXRXX_SFQS,SW_TZF_TZFXX_SFQS,SW_BG_FRBGJJTS,SW_JCXX_SFGTGSH,SW_TZF_GQFSD,SW_WFWZ_JJYS,SW_BG_FRYDDH_12M,SW_BG_HY_DH,SW_BG_FR_DH"
    vallist=values.split(",")
    print(len(vallist))


    valia="alaba"
    print(valia.strip("a"))

    lists = os.listdir("E:\\test\\baogao\\20211013")  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime("E:\\test\\baogao\\20211013" + "\\" + fn))  # 按时间排序
    file_new = os.path.join("E:\\test\\baogao\\20211013", lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)

    lista=[]
    seta=set(lista)
    lista.append("时代的")
    lista.append("时代的")
    lista.append("呈现出v")
    setb=set(lista)
    print(list(reversed(lista)))
    print(type(seta))
    print(setb)

    #print(__import__(name='pyclass',fromlist=['callPorcCase']))
    aa="aAabcdzxx"
    list=[]
    dd=aa.join(list)
    print(dd)
    aa="987654321"
    if "987654" in aa:
        aa=int(aa)+1
    print(aa)

    aax={"xx":{"zhibiaopass":0,"zhibiaoerror":1}}

    try:
        aa=[1,2]
        bb=aa[2]
    except Exception as e:
        print(e)
        print(123)
        ffc=traceback.format_exc()
        print(ffc)

    # user_info = {'a': 'letian', 'b': '123'}
    # r = requests.post("http://127.0.0.1:8080/add", json=user_info)
    #
    # print(r.headers)
    # print(r.text)

    # file_data = {'image': open('Lenna.jpg', 'rb')}
    #
    # user_info = {'info': 'Lenna'}
    #
    # r = requests.post("http://127.0.0.1:8080/upload", data=user_info, files=file_data)
    #
    # print(r.text)

    aaxx="123*"
    aaxx=aaxx.replace("*",",")
    print(aaxx)


    sss="""{'数据编号2，纳税编号9144****219G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号3，纳税编号9144****4760': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：2,实际值：7', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：115551.06', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：2,实际值：7', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：3', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：3']}

{'数据编号4，纳税编号9144****0Q88': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号5，纳税编号9144****00XP': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号6，纳税编号9144****4456': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：151340.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：151340.0,实际值：0.0']}

{'数据编号7，纳税编号9144****1741': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号8，纳税编号9144****9649': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：1784279.5,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：788472.15,实际值：2572751.65']}

{'数据编号9，纳税编号9144****489W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号10，纳税编号9144****9657': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号11，纳税编号9144****FB0X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号12，纳税编号9144****9D57': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号13，纳税编号9144****800G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号14，纳税编号9144****08XW': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号15，纳税编号9144****99X7': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号16，纳税编号9144****DX37': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号17，纳税编号9144****8669': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1']}

{'数据编号18，纳税编号9144****2601': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号19，纳税编号9144****PJXC': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号20，纳税编号9144****086G': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：6', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：86732.41', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：6', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：5', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：8', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：8']}

{'数据编号21，纳税编号9144****151X': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号23，纳税编号9144****Y33M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号24，纳税编号9144****7065': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：9220591.91,实际值：2560727.13', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：6659864.78']}

{'数据编号25，纳税编号9144****785T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号26，纳税编号9144****685D': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号27，纳税编号9144****588Q': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：56000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号28，纳税编号9144****92XW': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：25164141.62,实际值：23379409.62', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：306579.98,实际值：2091311.98', 'SF_FH_BZXR_3Y_QY,期望值：4,实际值：5']}

{'数据编号29，纳税编号9144****T70P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号30，纳税编号9144****114D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号31，纳税编号9144****215K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号32，纳税编号9144****808H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号33，纳税编号9144****9358': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号34，纳税编号9144****4303': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号35，纳税编号9144****7409': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号36，纳税编号9144****35X8': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：3,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：3,实际值：4']}

{'数据编号37，纳税编号9144****18X0': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号38，纳税编号9144****6014': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_SXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号39，纳税编号9144****674Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号40，纳税编号9144****1A40': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号41，纳税编号9144****AH65': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：154500.0,实际值：79500.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：75000.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号42，纳税编号9144****320K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号43，纳税编号9144****8542': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号44，纳税编号9144****6356': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号45，纳税编号9144****975B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号46，纳税编号9144****2543': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号47，纳税编号9144****582G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号48，纳税编号9144****912X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号49，纳税编号9144****743U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号50，纳税编号9144****0430': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号51，纳税编号9144****246N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号52，纳税编号9144****001L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号53，纳税编号9144****6477': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：245000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：245000.0,实际值：0.0']}

{'数据编号54，纳税编号9144****802T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号55，纳税编号9144****3169': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号56，纳税编号9144****727W': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号57，纳税编号9144****BE80': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号58，纳税编号9144****50XD': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号59，纳税编号9144****6B1H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号60，纳税编号9144****452K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号61，纳税编号9144****7691': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号62，纳税编号9141****5P0N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号63，纳税编号9144****081L': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：3', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：3', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：2']}

{'数据编号64，纳税编号9144****45XH': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号65，纳税编号9144****8N0D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号66，纳税编号9144****87XF': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号67，纳税编号9144****268P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号68，纳税编号9144****WG06': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号69，纳税编号9144****0894': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号70，纳税编号9144****J20J': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号71，纳税编号9144****374X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号72，纳税编号9144****967J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：919869.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：919869.0']}

{'数据编号73，纳税编号9144****9C8B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号74，纳税编号9144****713X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号75，纳税编号9144****259J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：1210.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：1210.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号76，纳税编号9144****555N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号77，纳税编号9144****962T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号78，纳税编号9144****08XT': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号79，纳税编号9144****082X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号80，纳税编号9144****291X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号81，纳税编号9144****662M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号82，纳税编号9144****040K': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号83，纳税编号9144****273C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号84，纳税编号9144****U06F': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：2', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号85，纳税编号9144****770X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号86，纳税编号9144****282H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号87，纳税编号9144****472A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号88，纳税编号9144****C561': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号89，纳税编号9144****13XC': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：3', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号90，纳税编号9144****EP2B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号91，纳税编号9144****873W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号92，纳税编号9144****715X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号93，纳税编号9144****413M': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：15,实际值：20', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：270500.0,实际值：90438.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：1258077.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：14,实际值：19', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1']}

{'数据编号94，纳税编号9144****865L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号95，纳税编号9144****422Q': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：4']}

{'数据编号96，纳税编号9144****NG6A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号97，纳税编号9144****5059': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号98，纳税编号9144****7488': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号99，纳税编号9144****535T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号100，纳税编号9144****8MX6': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号101，纳税编号9144****106N': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号102，纳税编号9144****930B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号103，纳税编号9144****07XR': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：2,实际值：3', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：2,实际值：3']}

{'数据编号104，纳税编号9144****NG08': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号105，纳税编号9144****209W': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号106，纳税编号9144****3144': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号107，纳税编号9144****640J': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号108，纳税编号9144****989D': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：14', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：310420.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：314459.6', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：14', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：3']}

{'数据编号109，纳税编号9144****852P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号110，纳税编号9144****8094': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号111，纳税编号9144****6361': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号112，纳税编号9144****485U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号113，纳税编号9144****8779': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号114，纳税编号9144****256R': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号115，纳税编号9144****103J': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：2,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：180200.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：2,实际值：4', 'SF_FH_BZXR_3Y_QY,期望值：2,实际值：3', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号116，纳税编号9144****366B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号117，纳税编号9144****599K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：86648.84,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：86648.84']}

{'数据编号118，纳税编号9144****7664': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号119，纳税编号9144****GE2X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号120，纳税编号9144****976R': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号121，纳税编号9144****919A': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：1393365.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号122，纳税编号9144****661B': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：2']}

{'数据编号123，纳税编号9144****709R': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号124，纳税编号9144****072B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号125，纳税编号9144****715E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号126，纳税编号9144****504A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号127，纳税编号9144****951N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号128，纳税编号9144****405W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号129，纳税编号9144****9413': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：1,实际值：2']}

{'数据编号130，纳税编号9144****3246': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号131，纳税编号9144****AJ9X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号132，纳税编号9144****462H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号133，纳税编号9144****750X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号134，纳税编号9144****7387': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号135，纳税编号9144****214E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号136，纳税编号9144****021J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号137，纳税编号9144****571N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号138，纳税编号9144****894K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号139，纳税编号9144****378A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号140，纳税编号9144****1644': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：840210.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：840210.0,实际值：0.0']}

{'数据编号141，纳税编号9144****2094': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号142，纳税编号9144****204F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号143，纳税编号9144****218C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号144，纳税编号9144****0692': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号145，纳税编号9144****9703': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号146，纳税编号9144****038H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号147，纳税编号9144****734M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号148，纳税编号9144****22XQ': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号149，纳税编号9144****9245': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：1389041.82', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：4', 'SF_FH_BZXR_3Y_QY,期望值：1,实际值：3', 'SF_FH_JRQK_BG_2Y_QY,期望值：2,实际值：4', 'SF_FH_JRQK_YG_2Y_QY,期望值：2,实际值：3']}

{'数据编号150，纳税编号9144****4049': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号151，纳税编号9144****361Y': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：6,实际值：9', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：2140913.15,实际值：2708901.37', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：6,实际值：9', 'SF_FH_BZXR_1Y_QY,期望值：2,实际值：3', 'SF_FH_BZXR_3Y_QY,期望值：7,实际值：8']}

{'数据编号152，纳税编号9144****615L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号153，纳税编号9144****G442': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号154，纳税编号9144****899U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号155，纳税编号9144****47XF': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号156，纳税编号9144****910E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号157，纳税编号9144****256U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1']}

{'数据编号158，纳税编号9144****RC76': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号159，纳税编号9144****2091': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号160，纳税编号9144****3K07': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号161，纳税编号9144****753Y': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：3,实际值：5', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：3,实际值：5']}

{'数据编号162，纳税编号9144****5218': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号163，纳税编号9144****012B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号164，纳税编号9144****HT46': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号165，纳税编号9144****40XA': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号166，纳税编号9144****7619': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：748000.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：748000.0']}

{'数据编号167，纳税编号9144****QU8X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号168，纳税编号9144****8267': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号169，纳税编号9144****519L': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号170，纳税编号9144****716X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号171，纳税编号9144****Q52D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号172，纳税编号9144****550B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号173，纳税编号9144****9525': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号174，纳税编号9144****347G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号175，纳税编号9144****8524': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：7,实际值：8', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：7,实际值：8', 'SF_FH_BZXR_1Y_QY,期望值：3,实际值：4', 'SF_FH_BZXR_3Y_QY,期望值：5,实际值：6', 'SF_FH_XZGXF_5Y_QY,期望值：1,实际值：2']}

{'数据编号176，纳税编号9144****EK74': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号177，纳税编号9144****81X8': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号178，纳税编号9144****J859': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号179，纳税编号9144****107T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号180，纳税编号9144****2757': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号181，纳税编号9144****8043': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：5', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：9596.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：5', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1']}

{'数据编号182，纳税编号9144****ED84': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号183，纳税编号9144****133J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号184，纳税编号9144****3265': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：8,实际值：9', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：8,实际值：9']}

{'数据编号185，纳税编号9144****7T7J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号186，纳税编号9144****442C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号187，纳税编号9144****594T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号188，纳税编号9144****2251': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号189，纳税编号9144****3020': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号190，纳税编号9144****0747': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号191，纳税编号9144****786U': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号192，纳税编号9144****627M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号193，纳税编号9144****4320': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：1,实际值：2']}

{'数据编号194，纳税编号9144****605X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号195，纳税编号9144****271F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号196，纳税编号9144****707E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号197，纳税编号9144****817N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：2974940.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：310000.0,实际值：3284940.0']}

{'数据编号198，纳税编号9144****0C0D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号199，纳税编号9144****1776': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号200，纳税编号9144****386H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号201，纳税编号9144****1755': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号202，纳税编号9144****760W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号203，纳税编号9144****GR04': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：118767.04', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号204，纳税编号9144****29X9': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号205，纳税编号9144****2W6L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号206，纳税编号9144****9260': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号207，纳税编号9144****4307': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号208，纳税编号9144****6671': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号209，纳税编号9144****9518': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号210，纳税编号9144****G45B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号211，纳税编号9144****602F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号212，纳税编号9144****3822': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：1970310.37,实际值：1914240.37', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：849632.25,实际值：905702.25']}

{'数据编号213，纳税编号9144****480J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号214，纳税编号9144****119L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号215，纳税编号9144****1427': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号216，纳税编号9144****533F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号217，纳税编号9144****414H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号218，纳税编号9144****684W': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：3,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：41796.09', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：3,实际值：4']}

{'数据编号219，纳税编号9144****522U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号220，纳税编号9144****ED9G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号221，纳税编号9144****442Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号222，纳税编号9144****580J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号223，纳税编号9144****0520': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：3', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：4', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：4']}

{'数据编号224，纳税编号9144****074K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号225，纳税编号9144****TU2F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号226，纳税编号9144****U25F': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：10', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：438408.22', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：144857.76', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：8', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：3', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：5', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号227，纳税编号9144****965Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号228，纳税编号9144****6208': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号229，纳税编号9144****4061': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号230，纳税编号9144****BA4G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号231，纳税编号9144****977P': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号232，纳税编号9144****648G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号233，纳税编号9144****RE39': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号234，纳税编号9144****850R': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号235，纳税编号9144****630G': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：4', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号236，纳税编号9144****420J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号237，纳税编号9144****677L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号238，纳税编号9144****520U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号239，纳税编号9144****150L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号240，纳税编号9144****CC6J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号241，纳税编号9144****42X1': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：351028.6,实际值：64500.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：397550.0,实际值：684078.6']}

{'数据编号242，纳税编号9144****777C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号243，纳税编号9144****971A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号244，纳税编号9144****887T': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：4,实际值：23', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：61481.65', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：4,实际值：22', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：2', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：12', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：12']}

{'数据编号245，纳税编号9144****9138': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：4,实际值：14', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：342177.97,实际值：486472.83', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：83420.08', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：4,实际值：14', 'SF_FH_BZXR_1Y_QY,期望值：1,实际值：2', 'SF_FH_BZXR_3Y_QY,期望值：3,实际值：6', 'SF_FH_JRQK_BG_2Y_QY,期望值：1,实际值：3', 'SF_FH_JRQK_YG_2Y_QY,期望值：1,实际值：3']}

{'数据编号246，纳税编号9144****1797': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：17', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：40000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：343986.11', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：16', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：4', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：6', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：7']}

{'数据编号247，纳税编号9144****427N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号248，纳税编号9144****006C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号249，纳税编号9144****593U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：77958.78', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：188358.78,实际值：110400.0']}

{'数据编号250，纳税编号9144****BQ03': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号251，纳税编号9144****241K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号252，纳税编号9144****621N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号253，纳税编号9144****076A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号254，纳税编号9144****2331': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号255，纳税编号9144****097U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：272830.0,实际值：558560.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：285730.0,实际值：0.0']}

{'数据编号256，纳税编号9144****0749': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号257，纳税编号9144****990B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号258，纳税编号9144****UA36': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号259，纳税编号9144****2297': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号260，纳税编号9144****1047': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号261，纳税编号9144****4G6L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号262，纳税编号9144****483M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号263，纳税编号9144****670W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号264，纳税编号9144****T32T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号265，纳税编号9144****1065': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号266，纳税编号9144****722F': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号267，纳税编号9144****EU79': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号268，纳税编号9144****794W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号269，纳税编号9144****0477': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号270，纳税编号9144****287D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号271，纳税编号9144****467J': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_SXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_SXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号272，纳税编号9144****7497': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号273，纳税编号9144****H45X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号274，纳税编号9144****228M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号275，纳税编号9144****34X5': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号276，纳税编号9144****880Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号277，纳税编号9144****034K': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：2', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号278，纳税编号9144****E60D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号279，纳税编号9144****1374': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号280，纳税编号9144****7803': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号281，纳税编号9144****K96G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号282，纳税编号9144****2069': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号283，纳税编号9144****003W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_SXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号284，纳税编号9144****73X6': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号285，纳税编号9144****120X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号286，纳税编号9144****RX39': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号287，纳税编号9144****5051': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号288，纳税编号9144****6131': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号289，纳税编号9144****3620': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号290，纳税编号9144****748Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号291，纳税编号9144****600P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号292，纳税编号9144****345M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号293，纳税编号9144****256B': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：4,实际值：6', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：4,实际值：6']}

{'数据编号294，纳税编号9144****9X58': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：120000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：4', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：2', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号295，纳税编号9144****338E': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号296，纳税编号9144****731P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号297，纳税编号9144****271X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号298，纳税编号9144****461Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号299，纳税编号9144****561T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号300，纳税编号9144****PJ6U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号301，纳税编号9144****9326': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：2,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：2,实际值：4', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号302，纳税编号9144****PG2B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号303，纳税编号9144****8123': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：3']}

{'数据编号304，纳税编号9144****U936': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号305，纳税编号9144****9032': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号306，纳税编号9144****LT33': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号307，纳税编号9144****0614': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号308，纳税编号9144****G84K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号309，纳税编号9144****579K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号310，纳税编号9144****187P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号311，纳税编号9144****CW58': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：533157.5,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：625157.5,实际值：1158315.0']}

{'数据编号312，纳税编号9144****RM4T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号313，纳税编号9144****832A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号314，纳税编号9144****695D': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：5,实际值：6', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：1426241.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：1426241.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：6,实际值：7']}

{'数据编号315，纳税编号9144****122E': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号316，纳税编号9144****516L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号317，纳税编号9144****33XL': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号318，纳税编号9144****2154': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号319，纳税编号9144****KY5Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号320，纳税编号9144****28X3': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号321，纳税编号9144****4J3B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号322，纳税编号9144****470L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号323，纳税编号9144****6858': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：629339.89,实际值：316570.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：312769.89']}

{'数据编号324，纳税编号9144****619Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号325，纳税编号9144****099A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号326，纳税编号9144****HR5G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号327，纳税编号9144****41XM': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号328，纳税编号9144****114X': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号329，纳税编号9144****8876': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号330，纳税编号9144****1462': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号331，纳税编号9144****417G': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号332，纳税编号9144****3K3D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号333，纳税编号9144****R69T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号334，纳税编号9144****84XG': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号335，纳税编号9144****042R': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：162759.95', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号336，纳税编号9144****5398': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：25', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：6591787.84', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：190192.2', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：26', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：13', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：13']}

{'数据编号337，纳税编号9144****1358': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号338，纳税编号9144****078C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号339，纳税编号9144****9W1H': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号340，纳税编号9144****075U': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号341，纳税编号9144****368C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号342，纳税编号9144****Q07C': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：2', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号343，纳税编号9144****053N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号344，纳税编号9144****97X2': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号345，纳税编号9144****735R': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：2', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：3']}

{'数据编号346，纳税编号9144****3F91': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号347，纳税编号9144****274Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号348，纳税编号9144****1915': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：5,实际值：6', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：5,实际值：6']}

{'数据编号349，纳税编号9144****6631': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号350，纳税编号9144****BT5H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号351，纳税编号9144****215T': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号352，纳税编号9144****601T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号353，纳税编号9144****034W': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号354，纳税编号9144****B918': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号355，纳税编号9144****6638': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号356，纳税编号9144****9460': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号357，纳税编号9144****78X0': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号358，纳税编号9144****88X5': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号359，纳税编号9144****169L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号360，纳税编号9144****8780': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号361，纳税编号9144****0325': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号362，纳税编号9144****6M8T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号363，纳税编号9144****1124': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号364，纳税编号9144****329W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号365，纳税编号9144****9370': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号366，纳税编号9144****8XXA': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号367，纳税编号9144****377A': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：2,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：2,实际值：4']}

{'数据编号368，纳税编号9144****1924': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号369，纳税编号9144****T914': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号370，纳税编号9144****972T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号371，纳税编号9144****78XL': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号372，纳税编号9144****2437': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号373，纳税编号9144****8552': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号374，纳税编号9144****294L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：121300.0,实际值：181300.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：128000.0,实际值：68000.0']}

{'数据编号375，纳税编号9144****HB9H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号376，纳税编号9144****0929': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：10,实际值：11', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：10,实际值：11', 'SF_FH_BZXR_1Y_QY,期望值：2,实际值：3', 'SF_FH_BZXR_3Y_QY,期望值：8,实际值：9', 'SF_FH_JRQK_BG_2Y_QY,期望值：1,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：1,实际值：2']}

{'数据编号377，纳税编号9144****7X5B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号378，纳税编号9144****478F': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：200000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：4', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号379，纳税编号9144****265J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号380，纳税编号9144****4350': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号381，纳税编号9144****FA63': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号382，纳税编号9144****994L': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：5,实际值：8', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：1020000.0,实际值：5020000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：3946913.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：5,实际值：8', 'SF_FH_BZXR_3Y_QY,期望值：2,实际值：6', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：3']}

{'数据编号383，纳税编号9144****UG76': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号384，纳税编号9144****383A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号385，纳税编号9144****070J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号386，纳税编号9144****677D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号387，纳税编号9144****8383': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号388，纳税编号9144****87XA': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号389，纳税编号9144****225U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号390，纳税编号9144****632D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号391，纳税编号9144****562D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号392，纳税编号9144****K577': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：20,实际值：22', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：8905502.32,实际值：8724348.92', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：484000.0,实际值：665153.4', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：20,实际值：22']}

{'数据编号393，纳税编号9144****695N': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号394，纳税编号9144****902G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号395，纳税编号9144****054N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：3943583.2,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：3943583.2']}

{'数据编号396，纳税编号9144****505E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号397，纳税编号9144****222Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号398，纳税编号9144****8214': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号399，纳税编号9144****0817': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号400，纳税编号9144****YF6Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号401，纳税编号9144****203U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号402，纳税编号9144****89XA': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号403，纳税编号9144****944P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号404，纳税编号9144****121N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：1155350.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：1155350.0', 'SF_FH_XZGXF_5Y_QY,期望值：1,实际值：2']}

{'数据编号405，纳税编号9144****148D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号406，纳税编号9144****4703': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：2', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号407，纳税编号9144****9915': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号408，纳税编号9144****394W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号409，纳税编号9144****5640': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号410，纳税编号9144****008B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号411，纳税编号9144****5EXK': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号412，纳税编号9144****830J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号413，纳税编号9144****CU4L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号414，纳税编号9144****969T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号415，纳税编号9144****260K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号416，纳税编号9144****370K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：6212664.51,实际值：4679178.35', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：331936.0,实际值：1865422.16']}

{'数据编号417，纳税编号9144****A69F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号418，纳税编号9144****R30E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：4,实际值：5']}

{'数据编号419，纳税编号9144****U14F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号421，纳税编号9144****A30H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号422，纳税编号9144****0K9M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号423，纳税编号9144****6591': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号424，纳税编号9144****344F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号425，纳税编号9144****YM43': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号426，纳税编号9144****451W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号427，纳税编号9144****532R': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号428，纳税编号9144****E83B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号429，纳税编号9144****222X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号430，纳税编号9144****612E': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：5', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：4']}

{'数据编号431，纳税编号9144****179Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号432，纳税编号9144****PU1F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号433，纳税编号9144****407P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号434，纳税编号9144****5625': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号435，纳税编号9144****16XB': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号436，纳税编号9144****797A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号437，纳税编号9144****966T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号438，纳税编号9144****1071': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：7194646.0,实际值：8413518.2', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：1218872.2,实际值：0.0']}

{'数据编号439，纳税编号9144****823M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号440，纳税编号9144****426X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：2498147.51,实际值：7945114.86', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：5446967.35,实际值：0.0']}

{'数据编号441，纳税编号9144****29XU': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号442，纳税编号9144****2879': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号443，纳税编号9144****JP6E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号444，纳税编号9144****259N': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号445，纳税编号9144****548A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_SXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_SXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号446，纳税编号9144****313C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号447，纳税编号9144****9165': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号448，纳税编号9144****963D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号449，纳税编号9144****121K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：295758.0,实际值：200630.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：95128.0', 'SF_FH_BZXR_3Y_QY,期望值：2,实际值：3', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1']}

{'数据编号450，纳税编号9144****535P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号451，纳税编号9144****6657': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号452，纳税编号9144****08XC': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：11,实际值：12', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：11,实际值：12']}

{'数据编号453，纳税编号9144****0258': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号454，纳税编号9144****9103': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号455，纳税编号9144****587M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号456，纳税编号9144****4C6D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号457，纳税编号9144****540H': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：3,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：330000.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：330000.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：3,实际值：4', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：2', 'SF_FH_BZXR_3Y_QY,期望值：1,实际值：7', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：4', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：4']}

{'数据编号458，纳税编号9144****0728': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号459，纳税编号9144****52X7': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号460，纳税编号9144****794P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号461，纳税编号9144****277W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号462，纳税编号9144****211P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号463，纳税编号9144****1W5J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号464，纳税编号9144****777U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号465，纳税编号9144****99X6': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号466，纳税编号9144****823E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号467，纳税编号9144****797G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号468，纳税编号9144****89XM': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号469，纳税编号9144****784L': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：5', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：120000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：4', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：3', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号470，纳税编号9144****071G': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号471，纳税编号9144****AT1W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号472，纳税编号9144****520E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号473，纳税编号9144****730F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_SXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_SXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号474，纳税编号9144****408U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号475，纳税编号9144****394L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号476，纳税编号9144****96X5': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号477，纳税编号9144****1239': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号478，纳税编号9144****1F3N': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：3', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：3', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：3', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：6', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：2']}

{'数据编号479，纳税编号9144****141M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号480，纳税编号9144****LK05': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号481，纳税编号9144****F66T': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号482，纳税编号9144****0124': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号483，纳税编号9144****944X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号484，纳税编号9144****662Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号485，纳税编号9144****1601': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：436524.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：436524.0,实际值：0.0']}

{'数据编号486，纳税编号9144****146T': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号487，纳税编号9144****598K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号488，纳税编号9144****9048': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号489，纳税编号9144****PM9H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号490，纳税编号9144****033M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号491，纳税编号9144****C71U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号492，纳税编号9144****285D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号493，纳税编号9144****0816': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号494，纳税编号9144****418N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号495，纳税编号9144****687H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号496，纳税编号9144****U97T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号497，纳税编号9144****6926': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号498，纳税编号9144****7BXN': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号499，纳税编号9144****J797': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号500，纳税编号9144****4663': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号501，纳税编号9144****302H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号502，纳税编号9144****2633': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号503，纳税编号9144****GK5K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号504，纳税编号9144****7694': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号505，纳税编号9144****28XG': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号506，纳税编号9144****648Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号507，纳税编号9144****542G': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：2,实际值：4', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：88150.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：2,实际值：4']}

{'数据编号508，纳税编号9144****55XG': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号509，纳税编号9144****755Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号510，纳税编号9144****6494': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号511，纳税编号9144****008W': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：2']}

{'数据编号512，纳税编号9144****4494': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号513，纳税编号9144****Y0XC': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号514，纳税编号9144****6350': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号515，纳税编号9144****572D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号516，纳税编号9144****4434': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号517，纳税编号9144****46XQ': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号518，纳税编号9144****3T21': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号519，纳税编号9144****688X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号520，纳税编号9144****340F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：528328.36,实际值：578901.23', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：6704361.3,实际值：6653788.43']}

{'数据编号521，纳税编号9144****2015': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号522，纳税编号9144****571P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号523，纳税编号9144****X86X': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：2000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号524，纳税编号9144****066P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号525，纳税编号9144****028K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号526，纳税编号9144****9827': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号527，纳税编号9144****PL9T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号528，纳税编号9144****7C97': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号529，纳税编号9144****7R41': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号530，纳税编号9144****483A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号531，纳税编号9144****228Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号532，纳税编号9144****789A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号533，纳税编号9144****308H': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：8', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：933401.14', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：8', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_SXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_SXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号534，纳税编号9144****708T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号535，纳税编号9144****G37T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号536，纳税编号9144****005U': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：13,实际值：15', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：40000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：40000.0,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：13,实际值：15']}

{'数据编号537，纳税编号9144****080Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号538，纳税编号9144****135N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号539，纳税编号9144****324X': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号540，纳税编号9144****70XL': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：2,实际值：3', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：2,实际值：3', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号541，纳税编号9144****596U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_XZGXF_5Y_QY,期望值：0,实际值：1']}

{'数据编号542，纳税编号9144****3482': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号543，纳税编号9144****487D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号544，纳税编号9144****3490': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号545，纳税编号9144****445Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号546，纳税编号9144****DD53': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号547，纳税编号9144****W7XF': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：3', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：3']}

{'数据编号548，纳税编号9144****6C7E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号549，纳税编号9144****5007': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号551，纳税编号9144****031U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号552，纳税编号9144****1967': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号553，纳税编号9144****QE2U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号554，纳税编号9144****UP4U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号555，纳税编号9144****Y42M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号556，纳税编号9144****991M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号557，纳税编号9144****807T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号558，纳税编号9144****506U': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号559，纳税编号9144****833T': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号560，纳税编号9144****456D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：7013057.86,实际值：6115040.06', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：898017.8']}

{'数据编号561，纳税编号9144****762W': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：5,实际值：6', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：5,实际值：6']}

{'数据编号562，纳税编号9144****544D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号563，纳税编号9144****12XB': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号564，纳税编号9144****3UXB': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：7', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：7']}

{'数据编号565，纳税编号9144****RQ4R': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号566，纳税编号9144****427K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号567，纳税编号9144****4064': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号568，纳税编号9144****790N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号569，纳税编号9144****448H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号570，纳税编号9144****C87M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号571，纳税编号9144****308E': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号572，纳税编号9144****7078': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号573，纳税编号9144****8772': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号574，纳税编号9144****3K1J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号575，纳税编号9144****WW59': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号576，纳税编号9144****6M7B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号577，纳税编号9144****1906': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：2', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：433446.94,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：433446.94', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：2', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：2']}

{'数据编号578，纳税编号9144****8168': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号579，纳税编号9144****194X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号580，纳税编号9144****392B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：1578535.0,实际值：1148809.5', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：305949.0,实际值：735674.5']}

{'数据编号581，纳税编号9144****P25B': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号582，纳税编号9144****1306': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号583，纳税编号9144****148Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：14111.79', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：14111.79,实际值：0.0']}

{'数据编号584，纳税编号9144****908Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：51200.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：51200.0']}

{'数据编号585，纳税编号9144****1218': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号586，纳税编号9144****132U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号587，纳税编号9144****5C9C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号588，纳税编号9144****296Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号589，纳税编号9144****391K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号590，纳税编号9144****968G': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号591，纳税编号9144****86XT': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：241540.0,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：241540.0']}

{'数据编号592，纳税编号9144****18XK': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号593，纳税编号9144****4099': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号594，纳税编号9144****422F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号595，纳税编号9144****7QXT': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号596，纳税编号9144****4459': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号597，纳税编号9144****644L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号598，纳税编号9144****309D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号599，纳税编号9144****144M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号600，纳税编号9144****0N5W': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号601，纳税编号9144****644J': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：1629.2', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号602，纳税编号9144****206K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号603，纳税编号9144****H849': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：250000.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：250000.0,实际值：0.0']}

{'数据编号604，纳税编号9144****66XF': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号605，纳税编号9144****438E': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号606，纳税编号9144****K940': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号607，纳税编号9144****95X4': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号608，纳税编号9144****9U8Q': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号609，纳税编号9144****8495': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号610，纳税编号9144****9708': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号611，纳税编号9144****4585': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号612，纳税编号9144****W88E': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号613，纳税编号9144****2619': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号614，纳税编号9144****496L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号615，纳税编号9144****18XU': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号616，纳税编号9144****127Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：2', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：5', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：5']}

{'数据编号617，纳税编号9144****230J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号618，纳税编号9144****HH4L': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号619，纳税编号9144****101U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号620，纳税编号9144****046H': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号621，纳税编号9144****EM27': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号622，纳税编号9144****058N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号623，纳税编号9144****2047': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号624，纳税编号9144****013Y': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号625，纳税编号9144****470J': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号626，纳税编号9144****826K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号627，纳税编号9144****3M9F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号628，纳税编号9144****08XF': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号629，纳税编号9144****2450': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号630，纳税编号9144****519Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号631，纳税编号9144****M53C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号632，纳税编号9144****K60K': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号633，纳税编号9144****0W2P': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号634，纳税编号9144****2500': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号635，纳税编号9144****R52N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：800000.0,实际值：889060.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：89060.0,实际值：0.0']}

{'数据编号636，纳税编号9144****0260': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号637，纳税编号9144****6R9T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号638，纳税编号9144****8805': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号639，纳税编号9144****UU6X': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号640，纳税编号9144****598T': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号641，纳税编号9144****660U': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号642，纳税编号9144****LX08': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号643，纳税编号9144****49XU': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号644，纳税编号9144****WL9A': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：306383.06,实际值：501787.86', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：195404.8,实际值：0.0']}

{'数据编号645，纳税编号9144****947Q': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号646，纳税编号9144****675C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号647，纳税编号9144****005N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号648，纳税编号9144****8525': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号649，纳税编号9144****K464': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：1,实际值：5', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：2855430.0,实际值：3668670.92', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：1,实际值：5']}

{'数据编号650，纳税编号9144****638Y': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：9,实际值：10', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：9,实际值：10', 'SF_FH_SXR_1Y_QY,期望值：0,实际值：1', 'SF_FH_SXR_3Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_JRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号651，纳税编号9144****267W': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号652，纳税编号9144****H79U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号653，纳税编号9144****149M': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号654，纳税编号9144****37XR': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号655，纳税编号9144****090Y': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1', 'SF_FH_BZXR_3Y_QY,期望值：0,实际值：4', 'SF_FH_SXR_3Y_QY,期望值：0,实际值：1']}

{'数据编号656，纳税编号9144****W99D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号657，纳税编号9144****766F': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号658，纳税编号9144****P46C': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号659，纳税编号9144****3158': ['SF_FH_FLDJFJRQK_BG_2Y_QY,期望值：0,实际值：1', 'SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_YG_2Y_QY,期望值：0,实际值：1']}

{'数据编号660，纳税编号9144****43XX': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号661，纳税编号9144****046N': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号662，纳税编号9144****424G': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_BZXR_1Y_QY,期望值：2,实际值：4', 'SF_FH_BZXR_3Y_QY,期望值：3,实际值：5']}

{'数据编号663，纳税编号9144****131D': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号664，纳税编号9144****TH0U': ['SF_FH_FLDJFJRQK_XAJE_BG_2Y_QY,期望值：None,实际值：0.0', 'SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}

{'数据编号665，纳税编号9144****5019': ['SF_FH_FLDJFJRQK_XAJE_YG_2Y_QY,期望值：None,实际值：0.0']}"""

    dxc=sss.split("\n")
    ffx=[]
    list1 = []
    map1 = {}
    list2 = []
    map2 = {}
    for isd in dxc:
        if isd=="":
            pass
        else:
            ffx.append(isd)
    for xcz in ffx:
        print(xcz)
        discc=eval(xcz)
        for keys in discc.keys():
            print(keys.split("纳税编号")[1])
            dsvalue = discc[keys]
            print(dsvalue)
            for ls in dsvalue:
                map1 = {}
                map1["税号"] = keys.split("纳税编号")[1]
                map1["不一致指标"] = ls.split(",")[0]
                map1["期望和实际值"] = ls.split(",")[1] + "," + ls.split(",")[2]
                print(ls.split(",")[0])
                print(ls.split(",")[1] + "," + ls.split(",")[2])
                list1.append(map1)
    print(len(list1))
    map2["sheet"]=list1
    list2.append(map2)
    fe.getExcel(list2)
    # dsxw={'数据编号3316，纳税编号9144****8XXA': ['SW_SDSNB_RJJCDLQYLX,期望值：None,实际值：0', 'SW_SDSNB_GXJSQY_KJRYBQYZGZS,期望值：0.4615,实际值：46.15']}
    # print(type(dsxw))
    # list1=[]
    # map1={}
    # list2=[]
    # map2={}
    # for keys in dsxw.keys():
    #     print(keys.split("纳税编号")[1])
    #     dsvalue=dsxw[keys]
    #     print(dsvalue)
    #     for ls in dsvalue:
    #         map1 = {}
    #         map1["税号"]=keys.split("纳税编号")[1]
    #         map1["不一致指标"]=ls.split(",")[0]
    #         map1["期望和实际值"]=ls.split(",")[1]+","+ls.split(",")[2]
    #         print(ls.split(",")[0])
    #         print(ls.split(",")[1]+","+ls.split(",")[2])
    #         list1.append(map1)
    # print(list1)
    print(10000/3600)
    shrd="""SW_SB_AYLJDY0_12M
    SW_SB_AYLJDY0_24M
    SW_SB_BBJJSC_ZZS_01Y
    SW_SB_LJNS0_01M
    SW_SB_LJNS0_02M
    SW_SB_LJNS0_03M
    SW_SB_LJNS0_06M
    SW_SB_LJNS0_09M
    SW_SB_LJNS0_12M
    SW_SB_LJNS0_15M
    SW_SB_LJNS0_18M
    SW_SB_LJNS0_21M
    SW_SB_LJNS0_24M
    SW_SB_LJSB0_01M
    SW_SB_LJSB0_02M
    SW_SB_LJSB0_03M
    SW_SB_LJSB0_03Q
    SW_SB_LJSB0_06M
    SW_SB_LJSB0_06M_Y
    SW_SB_LJSB0_09M
    SW_SB_LJSB0_12M
    SW_SB_LJSB0_13_24M
    SW_SB_LJSB0_15M
    SW_SB_LJSB0_18M
    SW_SB_LJSB0_21M
    SW_SB_LJSB0_24M
    SW_SB_LSXS_01M
    SW_SB_LSXS_02M
    SW_SB_LSXS_03M
    SW_SB_LSXS_06M
    SW_SB_LSXS_06M_X
    SW_SB_LSXS_06M_Y
    SW_SB_LSXS_09M
    SW_SB_LSXS_12M
    SW_SB_LSXS_12M_M
    SW_SB_LSXS_12M_Y
    SW_SB_LSXS_15M
    SW_SB_LSXS_18M
    SW_SB_LSXS_21M
    SW_SB_LSXS_24M
    SW_SB_NSYFS
    SW_SB_NSZE_QYSDS_01M
    SW_SB_NSZE_QYSDS_02M
    SW_SB_NSZE_QYSDS_03M
    SW_SB_NSZE_QYSDS_06M
    SW_SB_NSZE_QYSDS_09M
    SW_SB_NSZE_QYSDS_12M
    SW_SB_NSZE_QYSDS_15M
    SW_SB_NSZE_QYSDS_18M
    SW_SB_NSZE_QYSDS_21M
    SW_SB_NSZE_QYSDS_24M
    SW_SB_NSZE_XFS_01M
    SW_SB_NSZE_XFS_02M
    SW_SB_NSZE_XFS_03M
    SW_SB_NSZE_XFS_06M
    SW_SB_NSZE_XFS_09M
    SW_SB_NSZE_XFS_12M
    SW_SB_NSZE_XFS_15M
    SW_SB_NSZE_XFS_18M
    SW_SB_NSZE_XFS_21M
    SW_SB_NSZE_XFS_24M
    SW_SB_NSZE_ZZL_ZZS_12M_Y
    SW_SB_NSZE_ZZS_01M
    SW_SB_NSZE_ZZS_02M
    SW_SB_NSZE_ZZS_03M
    SW_SB_NSZE_ZZS_06M
    SW_SB_NSZE_ZZS_09M
    SW_SB_NSZE_ZZS_12M
    SW_SB_NSZE_ZZS_15M
    SW_SB_NSZE_ZZS_18M
    SW_SB_NSZE_ZZS_21M
    SW_SB_NSZE_ZZS_24M
    SW_SB_NSZE_ZZSQYSDS_01M
    SW_SB_NSZE_ZZSQYSDS_02M
    SW_SB_NSZE_ZZSQYSDS_03M
    SW_SB_NSZE_ZZSQYSDS_06M
    SW_SB_NSZE_ZZSQYSDS_09M
    SW_SB_NSZE_ZZSQYSDS_12M
    SW_SB_NSZE_ZZSQYSDS_15M
    SW_SB_NSZE_ZZSQYSDS_18M
    SW_SB_NSZE_ZZSQYSDS_21M
    SW_SB_NSZE_ZZSQYSDS_24M
    SW_SB_NSZEHBZZL_ZZSQYSDS_12M
    SW_SB_NSZEZZL_QYSDS_03M
    SW_SB_NSZEZZL_ZZSQYSDS_12M_A
    SW_SB_PJTQSBTS_ZZS_06M
    SW_SB_PJTQSBTS_ZZS_12M
    SW_SB_QBXSE_01M
    SW_SB_QBXSE_01Q
    SW_SB_QBXSE_02M
    SW_SB_QBXSE_02Q
    SW_SB_QBXSE_03M
    SW_SB_QBXSE_03Q
    SW_SB_QBXSE_06M
    SW_SB_QBXSE_09M
    SW_SB_QBXSE_12M
    SW_SB_QBXSE_15M
    SW_SB_QBXSE_18M
    SW_SB_QBXSE_21M
    SW_SB_QBXSE_24M
    SW_SB_QBXSE_NHZZL_DT_03M
    SW_SB_QBXSEB_01Q_12M
    SW_SB_QBXSEDTZZL_06M_A
    SW_SB_QBXSEHBZZL_03M
    SW_SB_QBXSEHBZZL_03M_A
    SW_SB_QBXSEHBZZL_06M_A
    SW_SB_QBXSEHYPLD_06M
    SW_SB_QBXSEXYDY5Q_ZDLXYFS_12M
    SW_SB_QBXSEZZL_03M
    SW_SB_QBXSEZZL_03M_A
    SW_SB_QBXSEZZL_03M_AVG
    SW_SB_QBXSEZZL_03M_Y
    SW_SB_QBXSEZZL_04_06_A
    SW_SB_QBXSEZZL_06M
    SW_SB_QBXSEZZL_06M_A
    SW_SB_QBXSEZZL_06M_AVG
    SW_SB_QBXSEZZL_06M_Y
    SW_SB_QBXSEZZL_07_12_A
    SW_SB_QBXSEZZL_12M
    SW_SB_QBXSEZZL_12M_A
    SW_SB_QBXSEZZL_12M_AVG
    SW_SB_QBXSEZZL_12M_Y
    SW_SB_SB0_JJYFS_01Q
    SW_SB_SBRQJGZDTS_ZZS
    SW_SB_SBRQJGZDTS_ZZS_01Y
    SW_SB_SBXX_SFQS
    SW_SB_SCSB
    SW_SB_SCSB_XKF
    SW_SB_SCSBYJL
    SW_SB_SFL_ZZSQYSDS_12M_A
    SW_SB_SFLHY_A
    SW_SB_SSSQZ_MAX
    SW_SB_SSSQZ_MIN
    SW_SB_YNSE_ZZL_ZZS_06M_Y
    SW_SB_YNSE_ZZS_01M
    SW_SB_YNSE_ZZS_02M
    SW_SB_YNSE_ZZS_03M
    SW_SB_YNSE_ZZS_06M
    SW_SB_YNSE_ZZS_09M
    SW_SB_YNSE_ZZS_12M
    SW_SB_YNSE_ZZS_15M
    SW_SB_YNSE_ZZS_18M
    SW_SB_YNSE_ZZS_21M
    SW_SB_YNSE_ZZS_24M
    SW_SB_YQSB_QYSDS_01M
    SW_SB_YQSB_QYSDS_01M_M
    SW_SB_YQSB_QYSDS_02M
    SW_SB_YQSB_QYSDS_02M_M
    SW_SB_YQSB_QYSDS_03M
    SW_SB_YQSB_QYSDS_03M_M
    SW_SB_YQSB_QYSDS_06M
    SW_SB_YQSB_QYSDS_06M_M
    SW_SB_YQSB_QYSDS_09M
    SW_SB_YQSB_QYSDS_09M_M
    SW_SB_YQSB_QYSDS_12M
    SW_SB_YQSB_QYSDS_12M_M
    SW_SB_YQSB_QYSDS_15M
    SW_SB_YQSB_QYSDS_15M_M
    SW_SB_YQSB_QYSDS_18M
    SW_SB_YQSB_QYSDS_18M_M
    SW_SB_YQSB_QYSDS_21M
    SW_SB_YQSB_QYSDS_21M_M
    SW_SB_YQSB_QYSDS_24M
    SW_SB_YQSB_QYSDS_24M_M
    SW_SB_YQSB_ZZS_01M
    SW_SB_YQSB_ZZS_01M_M
    SW_SB_YQSB_ZZS_02M
    SW_SB_YQSB_ZZS_02M_M
    SW_SB_YQSB_ZZS_03M
    SW_SB_YQSB_ZZS_03M_M
    SW_SB_YQSB_ZZS_06M
    SW_SB_YQSB_ZZS_06M_M
    SW_SB_YQSB_ZZS_09M
    SW_SB_YQSB_ZZS_09M_M
    SW_SB_YQSB_ZZS_12M
    SW_SB_YQSB_ZZS_12M_M
    SW_SB_YQSB_ZZS_15M
    SW_SB_YQSB_ZZS_15M_M
    SW_SB_YQSB_ZZS_18M
    SW_SB_YQSB_ZZS_18M_M
    SW_SB_YQSB_ZZS_21M
    SW_SB_YQSB_ZZS_21M_M
    SW_SB_YQSB_ZZS_24M
    SW_SB_YQSB_ZZS_24M_M
    SW_SB_YQSB_ZZSSDS_01M
    SW_SB_YQSB_ZZSSDS_01M_M
    SW_SB_YQSB_ZZSSDS_02M
    SW_SB_YQSB_ZZSSDS_02M_M
    SW_SB_YQSB_ZZSSDS_03M
    SW_SB_YQSB_ZZSSDS_03M_M
    SW_SB_YQSB_ZZSSDS_06M
    SW_SB_YQSB_ZZSSDS_06M_M
    SW_SB_YQSB_ZZSSDS_09M
    SW_SB_YQSB_ZZSSDS_09M_M
    SW_SB_YQSB_ZZSSDS_12M
    SW_SB_YQSB_ZZSSDS_12M_M
    SW_SB_YQSB_ZZSSDS_15M
    SW_SB_YQSB_ZZSSDS_15M_M
    SW_SB_YQSB_ZZSSDS_18M
    SW_SB_YQSB_ZZSSDS_18M_M
    SW_SB_YQSB_ZZSSDS_21M
    SW_SB_YQSB_ZZSSDS_21M_M
    SW_SB_YQSB_ZZSSDS_24M
    SW_SB_YQSB_ZZSSDS_24M_M
    SW_SB_YQWSB
    SW_SB_YQWSB_02Q
    SW_SB_ZDLXNS0_01M
    SW_SB_ZDLXNS0_02M
    SW_SB_ZDLXNS0_03M
    SW_SB_ZDLXNS0_06M
    SW_SB_ZDLXNS0_09M
    SW_SB_ZDLXNS0_12M
    SW_SB_ZDLXNS0_15M
    SW_SB_ZDLXNS0_18M
    SW_SB_ZDLXNS0_21M
    SW_SB_ZDLXNS0_24M
    SW_SB_ZDLXSB0_01M
    SW_SB_ZDLXSB0_02M
    SW_SB_ZDLXSB0_03M
    SW_SB_ZDLXSB0_06M
    SW_SB_ZDLXSB0_09M
    SW_SB_ZDLXSB0_12M
    SW_SB_ZDLXSB0_13_24M
    SW_SB_ZDLXSB0_15M
    SW_SB_ZDLXSB0_18M
    SW_SB_ZDLXSB0_21M
    SW_SB_ZDLXSB0_24M
    SW_SB_ZJSBJJYFS"""
    print(",".join(shrd.split("\n")))
    alllist=shrd.split("\n")
    i=0
    sal=""
    for ali in alllist:
        i+=1
        sal+=ali.strip()+","
        print(i)
    print(sal[:-1])
    print(len(sal[:-1].split(",")))

    print(6300/31)
    ur="http://192.168.81.55/svn/vzoomdoc/%E5%A4%96%E9%83%A8%E9%93%B6%E8%A1%8C%E6%9B%B4%E6%96%B0%E5%8C%85/%e5%ae%81%e5%a4%8f%e9%93%b6%e8%a1%8c/2020-10-21%e8%b4%b7%e5%90%8e%e5%8f%8d%e9%a6%88/20211130%e8%b4%b7%e5%90%8e%e5%8f%8d%e9%a6%88/"
    print(ur.encode("gbk").decode("utf-8"))

    df="""913303826725100024
913206917596100018
913410046104100025
91340103MA2N100026
913506280953100027
91469006MA5T100049
91460200MA5T100050
913502050511100044
911408296942100045
914107023956100002
914301023293100010
91442000MA4W100015
914208023317100004
914203040554100003
914201125848100005
914302005910100009
91410221MA45100001
914201036823100006
91420800MA48100007
91430104MA4M100011
91430281MA4L100008
914406067398100012
914419003151100013
914403005598100014
913202045837100019
91320113MA1W100020
913611233225100029
914109000559100034
913501001543100041
913506240561100042
913501007983100043
913607027969100028
913201150626100016
91360402MA38100030
91411503MA44100031
91410225MA44100035
913301220888100021
913307815985100022
914107817906100032
91341825MA2M100036
92340802MA2P100037
913401005663100038
913306047434100023
913204125855100017
914114036728100033
91341222MA2M100039
913506813157100040
914403003564100046
914403001922100047
91450100MA5L100048
916101037974100058
91532623MA6K100055
913202827394100061
91430111MA4P100062
91440116MA59100063
914406003382100067
91610400MA6X100059
913204126896100060
914503007399100068
914501073402100069
914501033158100070
914690333240100071
915301030615100056
91533123MA6K100057
914601000563100051
913502060793101107
911201110937101093
91411423L108101113
91410100MA3X101114
914107043268101115
913416230852101108
913415000933101109
913405217964101110
913401000709101111
914200007612101116
914290040581101117
916101333337101088
913503047416101112
911202220668101094
913310035561101099
913413026789101100
91610131MA6U101089
93653121MA77101090
911201163006101095
913416003366101101
91340104MA2T101102
91340300MA2N101103
91341723MA2N101104
91652901MA78101091
914403000685100064
93500235MA60100052
915002297530100053
91532331MA6K100054
91440300MA5D100065
92440200MA4Y100066
91440300MA5F100718
914601000510100722
92440300MA5F100719
914504005718100720
914501025547100721
914401010746100716
92440300MA5D100717
91460100MA5T100723
91500105MA60100727
935301280776100728
91530902MA6N100729
915326250522100731
92530421MA6K100732
916109256847100734
935001145979100724
913502067841100735
91500101MA5Y100725
915340013252100730
91500114MA5Y100726
916103306611100733
913502136712100736
91411502MA40101077
914101843415101078
914201040630101080
914301047459101083
91430104MA4L101084
914307005870101085
91430211MA4P101087
913507007869100737
914112227919101074
914201020557101081
914116263172101075
91430281MA4M101086
914306826663101082
914101823958101076
914100004158101079
91330301MA28101097
913303810542101098
913206210502101096
91340111MA2N101105
913506240665101106
652828199306101092
913206126993101127
916590017817101134
914401115523101121
914403000769101122
913310023073101142
913301227708101143
913306046855101144
913303273255101145
913415250544100164
913401235845100165
91341102MA2M100166
91341500MA2T100167
913506287960100168
913508000750100169
913502066852100170
91361122MA39100258
91370830MA3Q100259
91410928MA46100260
91411222MA44100261
914116816897100262
913301107996100263
91330784MA28100264
91460200MA5T100265
92469027MA5T100266
91500229MA5U100267
91500108MA5Y100268
911201137491100366
911201120935100367
911201123004100368
91120222MA06100369
91652301MA77101135
913307025816101146
911202236877101147
911201165832101148
914301246735101118
914503007512101119
914403007675101123
913201922497101128
911201116603101136
91410102MA40101137
92440300MA5D101124
91460100MA5T101129
91410305MA3X101138
915002270605101130
914201116953101139
914403003593101125
915301007506101131
913208300747101126
92532925MA6K101132
91430424MA4P101140
91430121MA4P101120
91610425MA6X101133
913202116725101141
91131026MA08101154
91140830MA0G101159
911410005514101160
911201167548101149
914201151782101155
911201037128101150
91120104MA07101151
911201123005101152
911402126898101161
91130923MA07101156
91141081MA0K101162
91131026MA08101157
911301320581101158
91130982MA09101153
91500241MA5U100159
91500115MA5U100160
91341622MA2T100161
91341721MA2N100162
91341881MA2P100163
92120222L548100370
911201163004100371
92130408MA0A100372
91131082MA08100373
91130435MA0D100374
91440300MA5E100457
91530121MA6K100458
915301113252100459
91530100MA6K100460
915301127873100461
914110825596100462
914103817708100463
914110813417100464
914107006846100465
92411403MA41100466
914101056794100467
914101040981100468
91410500MA3X100469
914201113034100470
91430481MA4Q100471
914305293256100472
91500000MA60100520
91500118MA5U100521
912207216869100522
92220382MA15100523
912301996802100524
91321016MA1Y100525
913206846770100526
913205827481100527
913204133213100528
913202820782100529
913210123141100530
913203125985100531
913201066983100532
91330782MA28100533
91330782MA29100534
91330101MA27100535
91340225MA2R100536
913416003279100537
913504215747100538
91360600MA38100539
91430600MA4R100473
91450103MA5N100474
914508215843100475
92469002MA5R100476
915001133396100477
91500222MA5U100478
92500107MA5U100479
915002400949100480
915306216930100481
935301263466100482
915307225688100483
915301227928100484
92530102MA6N100485
916100007099100486
916103015778100487
916101336686100488
91610502MA6Y100489
916101036732100490
916100002942100491
91610139MA6W100492
92610303MA6X100493
916528016666100494
911310256652100495
91131022MA08100496
92130181MA0A100497
130729198508100498
91140100MA0H100499
912108115613100500
92210204MA0U100501
912202010646100502
91530103MA6L100503
916105210569100504
916101042206100505
91653101MA77100506
91653101MA77100507
916501025688100508
911202220865100509
91120113MA06100510
914407847436100511
91440605MA4U100512
914403000711100513
914503050907100514
92450100MA5N100515
914503210985100516
92500228MA60100517
91500113MA5Y100518
91500000MA5U100519
913709005978100540
913708837286100541
91130928MA07100542
912201040818100543
91220122MA17100544
91230103MA19100545
913101126822100546
913205080727100547
91450881MA5N100548
915001167093100549
915001045992100550
91530102MA6N100580
91610132MA6U100581
916100000679100582
914201120744100583
914201120908100584
914201007612100585
91422801MA49100586
91430408MA4Q100587
130128700745100588
91350104MA2Y100623
913505827869100624
913501025917100625
913502030899100626
913506235509100627
92360104MA36100628
91361102MA37100629
93410882MA40100630
91411502MA40100631
913304117154100632
913304210786100633
913406000739100634
91340223MA2P100635
911301300720100674
91500000MA5Y100551
913204125570100552
913205817596100553
91610302MA6X100554
92610133MA6W100555
610326199110100556
936528285688100557
911202235723100558
911201167522100559
911201013409100560
91131081MA0C100561
91131002MA08100562
911301085982100563
92130424MA09100564
911411255587100565
911402007701100566
92141028MA0H100567
932102135880100568
91210213MA0Q100569
912102045506100570
91500107MA5Y100571
91500106MA5U100572
91500000MA5U100573
91533103MA6N100574
91530723L123100575
915301110615100576
91530103MA6K100577
92530322MA6N100578
91320583MA1N100663
91320311MA1W100664
913311253076100665
913302005545100666
914104820862100667
92410100MA44100668
91410581MA44100669
92410185MA41100670
914209023165100671
914208816884100672
914205836980100673
915308000724100579
91130102MA08100675
91130802MA07100676
91430104MA4L100677
91430105MA4Q100678
92430211MA4P100679
91431125MA4P100680
914401130701100681
914403001921100682
914403007992100683
914408043150100684
911309233475100589
130635198409100590
92130982MA0D100591
91130102MA09100592
911407287485100593
92210203MA0Y100594
92210281MA0W100595
91210283MA0Q100596
92210231MA0U100597
912204007787100598
912202020540100599
912201816616100600
913404000723100636
911310267575100696
91130229MA09100697
931408220972100698
911401007435100699
92141031MA0H100700
91140522L010100701
911410813992100702
912203026051100703
92220101MA14100704
912207225650100705
91220524MA13100706
913209136696100611
913301005630100612
913301837620100613
92330182MA28100614
91331021MA29100615
913404007050100616
913402215888100617
913401230544100618
913406217865100619
91341126MA2M100620
913501046650100621
913502007054100622
913505823154100637
913502125878100638
913502125562100639
913505037937100640
91350526MA34100641
91370303MA3E100642
91370881MA3D100643
91371102MA3D100644
914104233449100645
914403003263100685
913506810622100686
914313220988100687
914305117808100688
91430400MA4L100689
914301245722100690
92430102MA4N100691
91431300MA4L100692
91430481MA4L100693
914301043528100694
91220101MA0Y100601
911202233005100602
911201126847100603
911202226661100604
52120110MJ05100605
931301310737100606
91130429L014100607
911309270932100608
91440300MA5D100609
913205067141100610
91411323MA44100646
412727397137100647
91410182MA45100648
91410403MA3X100649
91410423MA45100650
914103816794100651
91410721MA3X100652
914106006753100653
91420822MA48100654
91430100MA4L100695
91220105MA17100655
913101075820100656
913205062516100657
913204027332100658
913213225726100659
913205830502100660
913202816921100661
913205945911100662
912304005561100707
911408000519100375
91140109MA0K100376
91210212MA0Q100377
912103810762100378
913502067912100379
91341503MA2N100380
91340200MA2P100381
913400001490100382
913401005689100383
913501057318100384
91350213MA31100385
911202226974100081
91120116MA05100082
91130431MA09100083
911302307502100084
91130105MA07100085
911408023468100086
91141002MA0H100087
912102113973100088
91210202MA0Q100089
912202037171100090
912201226826100091
913205065810100180
913202007899100708
913206825837100709
913202037424100710
913210121407100711
913212837558100712
913206127615100713
91320902MA1Q100714
914419007545100715
915001077474100072
915001093460100073
915305240832100074
91530103MA6K100075"""
    dj=df.split("\n")
    print(dj)


    ccz="'SW_SB_YQSB_ZZS_03M_M', 'SW_SBZS_NSZE_ZZL_ZZS_03M', 'SW_SB_NSYFS', 'SW_CWBB_ZZCZZTS', 'SW_JCXX_NSRJCXX_SFQS', 'SW_CWBB_XSQLRL_M', 'SW_BG_HY_15M', 'SW_CWBB_LRZEZZLV', 'SW_CWBB_QTYWSRZZL', 'SW_SBZS_NSZE_ZZS_03M_M', 'SW_CWBB_JLRZCHJ', 'SW_SBZS_NSZE_ZZL_QYSDS_12M', 'SW_CWBB_ZEWBEBITDA', 'SW_CWBB_GLFZBL_QJ', 'SW_SB_ZDLXSB0_15M', 'SW_CWBB_ZZLRZZLV', 'SW_SB_YQSB_ZZSSDS_12M_M', 'SW_SB_SCSBYJL', 'SW_CWBB_ZZCZZL', 'SW_BG_FR_24M', 'SW_CWBB_LRZE', 'SW_BG_JYDZ_24M', 'SW_BG_HY_24M', 'SW_CWBB_YSZKZZTS', 'SW_CWBB_TZSY_1', 'SW_CWBB_GDZCBCL_A', 'SW_SBZS_NSZE_QYSDS_15M_M', 'SW_SBZS_NSZE_ZZS_09M_M', 'SW_CWBB_YYLRFZB', 'SW_CWBB_CHZZL_CB', 'SW_JCXX_NSRXYPJ', 'SW_SB_LJSB0_13_24M', 'SW_CWBB_JKSRB', 'SW_CWBB_SZZQZZZL', 'SW_SB_YQSB_QYSDS_02M_M', 'SW_SB_QBXSEDTZZL_06M_A', 'SW_SB_YQSB_ZZSSDS_01M_M', 'SW_SBZS_NSZE_QYSDS_09M_M', 'SW_SB_SBXX_SFQS', 'SW_SB_SFLHY_A', 'SW_BG_FR_06M', 'SW_SB_QBXSEHBZZL_03M_A', 'SW_BG_FR_12M', 'SW_BG_CWFZR_01M', 'SW_CWBB_YFZKZZL', 'SW_SB_YQSB_QYSDS_21M_M', 'SW_CWBB_XSJLL_2', 'SW_BG_HY_12M', 'SW_SB_YQSB_ZZS_21M_M', 'SW_CWBB_ZCJLL', 'SW_CWBB_ZZWSZBL', 'SW_CWBB_CHZZTS_CB', 'SW_CWBB_GDZCZZL', 'SW_WFWZ_01M', 'SW_SB_YQSB_QYSDS_01M_M', 'SW_WFWZ_18M', 'SW_SBZS_NSZE_QYSDS_21M_M', 'SW_SB_LSXS_21M', 'SW_SB_QBXSEZZL_12M_A', 'SW_SB_NSZEZZL_ZZSQYSDS_12M_A', 'SW_SBZS_NSZE_ZZS_21M_M', 'SW_BG_BSRY_12M', 'SW_BG_HY_18M', 'SW_CWBB_YHLXBS', 'SW_CWBB_ZZCBCL', 'SW_CWBB_JLR', 'SW_SB_QBXSEZZL_12M_AVG', 'SW_CWBB_ZCLRL', 'SW_SBZS_XWFKCS_21M', 'SW_SBZS_NSZE_ZZL_QYSDS_03M', 'SW_SBZS_NSZE_ZZSQYSDS_12M_M', 'SW_CWBB_DQJKBEBIT', 'SW_CWBB_MLLHY', 'SW_BG_FR_21M', 'SW_SBZS_NSZE_QYSDS_02M_M', 'SW_SBZS_NSZE_QYSDS_01M_M', 'SW_BG_FR_01M', 'SW_SB_QBXSE_03Q', 'SW_BG_JYDZ_03M', 'SW_SBZS_NSZEZZL_ZZSSDS_06M', 'SW_SBZS_NSZE_QYSDS_03M_M', 'SW_SB_ZDLXSB0_21M', 'SW_TZF_TZFXX_SFQS', 'SW_CWBB_LRZE_1', 'SW_SB_QBXSEZZL_03M_A', 'SW_SBZS_NSZE_ZZS_24M_M', 'SW_CWBB_YSZKZZBXSSRZZ', 'SW_CWBB_ZZLRZJKB_2', 'SW_SB_AYLJDY0_12M', 'SW_SB_YQSB_ZZS_02M_M', 'SW_BG_FR_09M', 'SW_SB_YQSB_QYSDS_12M_M', 'SW_SB_AYLJDY0_24M', 'SW_SBZS_NSZE_QYSDS_12M_M', 'SW_CWBB_ZSZKZZL', 'SW_CWBB_QTZWLRBL', 'SW_CWBB_ZCFZB_SSQQ_MIN', 'SW_SB_YQSB_ZZSSDS_15M_M', 'SW_CWBB_YUSZKZZL', 'SW_CWBB_SQXSJLL', 'SW_CWBB_LRSRBL_A', 'SW_CWBB_TZSY_2', 'SW_SB_YQSB_ZZSSDS_03M_M', 'SW_SBZS_NSZE_ZZS_18M_M', 'SW_CWBB_XSQLRL', 'SW_SBZS_NSZE_QYSDS_06M_M', 'SW_CWBB_ZZLRZJKB', 'SW_SB_QBXSEZZL_06M_AVG', 'SW_WFWZ_09M', 'SW_SB_ZJSBJJYFS', 'SW_CWBB_SQZZCJLL', 'SW_CWBB_JLRZZLV', 'SW_CWBB_YYLR_1', 'SW_BG_CWFZR_24M', 'SW_SB_YQSB_ZZS_15M_M', 'SW_SB_YQSB_ZZS_09M_M', 'SW_CWBB_ZCFZB_SFQS', 'SW_SB_YQSB_ZZSSDS_06M_M', 'SW_BG_JYDZ_12M', 'SW_WFWZ_12M', 'SW_CWBB_MLL', 'SW_WFWZ_15M', 'SW_LXR_LXRXX_SFQS', 'SW_BG_JYDZ_06M', 'SW_CWBB_ZZCZZL_1', 'SW_SBZS_NSZE_ZZS_02M_M', 'SW_SBZS_NSZE_ZZS_12M_M', 'SW_CWBB_LDZCYYSR', 'SW_CWBB_LDFZYYSR_QJ', 'SW_BG_FR_18M', 'SW_SB_QBXSEZZL_04_06_A', 'SW_SBZS_NSZE_ZZSQYSDS_24M_M', 'SW_SB_YQSB_ZZS_24M_M', 'SW_SB_YQSB_QYSDS_15M_M', 'SW_SB_ZDLXSB0_13_24M', 'SW_SB_ZDLXNS0_15M', 'SW_BG_HY_21M', 'SW_CWBB_YFZKZZTS', 'SW_SB_ZDLXSB0_18M', 'SW_BG_FRBGJJTS', 'SW_SB_YQSB_QYSDS_18M_M', 'SW_CWBB_SQLRL', 'SW_SB_ZDLXNS0_01M', 'SW_BG_HY_09M', 'SW_SB_ZDLXNS0_02M', 'SW_SB_YQSB_ZZSSDS_21M_M', 'SW_SB_YQSB_ZZS_06M_M', 'SW_CWBB_ZCJLL_1', 'SW_BG_CWFZR_06M', 'SW_CWBB_JZCSZLV', 'SW_CWBB_XJZHQ', 'SW_SBZS_ZJJKJJYFS', 'SW_CWBB_ZHZWFGB', 'SW_SB_YQSB_ZZSSDS_02M_M', 'SW_CWBB_JLR_1', 'SW_SB_ZDLXNS0_18M', 'SW_SBZS_NSZEZZL_ZZSSDS_12M', 'SW_SBZS_NSZE_ZZS_01M_M', 'SW_CWBB_JZCSZL_1', 'SW_CWBB_SZZQZZZTS', 'SW_CWBB_LRZE_2', 'SW_CWBB_LRB_SSQQ_MIN', 'SW_CWBB_XSJLL', 'SW_CWBB_HYYYSRCHB', 'SW_SB_YQSB_ZZS_01M_M', 'SW_CWBB_ZZCSZL', 'SW_CWBB_LDZCZZL', 'SW_CWBB_ZZCJLL', 'SW_CWBB_ZCZZLRLV', 'SW_SB_YQSB_ZZS_18M_M', 'SW_SB_YQSB_QYSDS_09M_M', 'SW_SB_QBXSE_NHZZL_DT_03M', 'SW_CWBB_SFYCB', 'SW_SBZS_NSZE_ZZS_15M_M', 'SW_SB_QBXSEZZL_06M_A', 'SW_SB_YQSB_QYSDS_06M_M', 'SW_WFWZ_21M', 'SW_CWBB_ZZWSRZZLV', 'SW_CWBB_YYLR', 'SW_SBZS_SBZSXX_SFQS', 'SW_SB_LSXS_15M', 'SW_CWBB_SQLRZJKB', 'SW_SB_ZDLXNS0_21M', 'SW_SBZS_NSZE_QYSDS_24M_M', 'SW_CWBB_GDZCZZL_1', 'SW_CWBB_XSQLRFZB', 'SW_SB_YQSB_ZZSSDS_24M_M', 'SW_WFWZ_24M', 'SW_WFWZ_03M', 'SW_SBZS_NHZZL_DT_ZZS_06M', 'SW_SB_YQSB_ZZS_12M_M', 'SW_SB_LSXS_12M', 'SW_CWBB_YYSRZZJKB', 'SW_CWBB_JLRSYZQY_QJ', 'SW_CWBB_JZCSZLZZLV', 'SW_CWBB_GLFYZCHJ_QJ', 'SW_WFWZ_02M', 'SW_SB_YQSB_QYSDS_24M_M', 'SW_CWBB_QTYSKBSSZBZBGJ', 'SW_CWBB_YYLR_2', 'SW_BG_CWFZR_12M', 'SW_CWBB_JLR_2', 'SW_CWBB_YYLRJJKB', 'SW_CWBB_ZSZKZZL_2', 'SW_SB_YQSB_ZZSSDS_18M_M', 'SW_SBZS_NSZE_QYSDS_18M_M', 'SW_CWBB_LDZCZZL_1', 'SW_BG_HY_02M', 'SW_BG_FR_15M', 'SW_SBZS_NSZE_QYSDS_02M', 'SW_CWBB_SSZBSR', 'SW_CWBB_YSZKBXSSR', 'SW_SB_YQSB_QYSDS_03M_M', 'SW_SB_LSXS_18M', 'SW_CWBB_LXBZBS', 'SW_TZF_FRTZBL_HMXM', 'SW_CWBB_EBITBDQJK', 'SW_SB_QBXSEZZL_07_12_A', 'SW_CWBB_SZZQZZZL_1', 'SW_CWBB_GDZCZZL_A', 'SW_SBZS_NSZE_ZZS_06M_M', 'SW_CWBB_KCZSZKHDFZBL', 'SW_CWBB_TZSY', 'SW_CWBB_TZSZBL', 'SW_SB_QBXSEZZL_03M_AVG', 'SW_CWBB_LRB_SFQS', 'SW_SB_ZDLXSB0_02M', 'SW_CWBB_GDZCZZTS', 'SW_CWBB_LDZCZZTS', 'SW_SB_YQSB_ZZSSDS_09M_M', 'SW_CWBB_YYLRZJKB', 'SW_SB_ZDLXNS0_24M', 'SW_SB_LSXS_24M', 'SW_WFWZ_06M'"
    print(len(ccz.split(",")))


    print((213420.55+0.0)*5*0.3*0.9)

    sfcf="zxc"
    print(len(sfcf))