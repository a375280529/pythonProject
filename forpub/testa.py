#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
import os

import turtle
import jsonpath
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

    values="SW_CWBB_ZSBZSBL,SW_CWBB_XJLDFZL,SW_CWBB_LDBL,SW_CWBB_SDBL,SW_CWBB_ZCFZL,SW_CWBB_ZQFZL,SW_CWBB_CQBL,SW_CWBB_ZXJZZWL,SW_CWBB_YHLXBS,SW_CWBB_CQFZYYZJBL,SW_CWBB_ZZZJZWB,SW_CWBB_YXZCZWL,SW_CWBB_YHFZZCB,SW_CWBB_ZHZWFGB,SW_CWBB_ZHZWZBJZB,SW_CWBB_ZEWBEBITDA,SW_CWBB_CHLDFZB,SW_CWBB_XJBL,SW_CWBB_JKSRB,SW_CWBB_ZQJKSRB,SW_CWBB_DQJKSRB,SW_CWBB_QTZFKSRB,SW_CWBB_YFGZSRB,SW_CWBB_YFSJSRB,SW_CWBB_CQZBFZL,SW_CWBB_LXBZBS,SW_CWBB_EBITBDQJK,SW_CWBB_DQJKBEBIT,SW_CWBB_ZZLRZJKB,SW_CWBB_SRLXBZBS,SW_CWBB_XSQLRFZB,SW_CWBB_SQLRZJKB,SW_CWBB_YYLRZJKB,SW_CWBB_YYLRFZB,SW_CWBB_YYLRJJKB,SW_CWBB_ZZLRZJKB_2,SW_CWBB_KCZSZKHDFZBL,SW_CWBB_XJB,SW_CWBB_QZFZBL,SW_CWBB_LDZCZB,SW_CWBB_LDFZZB,SW_CWBB_GDZCQZBL,SW_CWBB_LDFZL,SW_CWBB_ZZZBZB,SW_CWBB_ZHFZJG,SW_CWBB_SZZQZBL,SW_CWBB_FXZWJGB,SW_CWBB_ZJKQYB,SW_CWBB_JJKQYB,SW_CWBB_FLDFZQZB,SW_CWBB_ZQFZZCB,SW_CWBB_ZZCZZL,SW_CWBB_ZSZKZZL,SW_CWBB_LDZCZZL,SW_CWBB_SZZQZZZL,SW_CWBB_GDZCZZL,SW_CWBB_CHZZL_CB,SW_CWBB_YFZKZZL,SW_CWBB_YYSRZZJKB,SW_CWBB_ZZCZZL_1,SW_CWBB_ZSZKZZL_2,SW_CWBB_LDZCZZL_1,SW_CWBB_SZZQZZZL_1,SW_CWBB_GDZCZZL_1,SW_CWBB_DQJKXJBL,SW_CWBB_SDZCZB,SW_CWBB_YYZBSRB,SW_CWBB_SRFYB,SW_CWBB_ZCLRL,SW_CWBB_ZZCSZL,SW_CWBB_ZZCJLL,SW_CWBB_ZZCBCL,SW_CWBB_ZCJLL,SW_CWBB_ZCJLL_1,SW_CWBB_SQXSJLL,SW_CWBB_SQZZCJLL,SW_CWBB_ZZMLL,SW_CWBB_XSJLL,SW_CWBB_XSFZBL,SW_CWBB_ZZWSZBL,SW_CWBB_TZSZBL,SW_CWBB_SXFZBL,SW_CWBB_QTZWLRBL,SW_CWBB_XSQLRL,SW_CWBB_GLFZBL,SW_CWBB_ZZSRCHB,SW_CWBB_ZSKZZZCBBL,SW_CWBB_CHZZZCBBL,SW_CWBB_ZFZKZZZCBBL,SW_CWBB_BWFZBL,SW_CWBB_SQLRL,SW_CWBB_JZCSZLV,SW_CWBB_ZCZZLRLV,SW_CWBB_JZCSZL_1,SW_CWBB_ZZCZZLV,SW_CWBB_ZZSRZZL,SW_CWBB_ZSZKTBZZL,SW_CWBB_YUSZKZZL,SW_CWBB_ZFKZZLV,SW_CWBB_CHTBZZLV,SW_CWBB_ZZLRZZLV,SW_CWBB_SZZQZZZLV,SW_CWBB_LRZEZZLV,SW_CWBB_JZCSZLZZLV,SW_CWBB_QTYWSRZZL,SW_CWBB_ZZWSRZZLV,SW_CWBB_JLRZZLV,SW_CWBB_GDZCZZLV,SW_CWBB_ZZCZZTS,SW_CWBB_YSZKZZTS,SW_CWBB_LDZCZZTS,SW_CWBB_SZZQZZZTS,SW_CWBB_GDZCZZTS,SW_CWBB_CHZZTS_CB,SW_CWBB_YFZKZZTS,SW_CWBB_XJZHQ,SW_CWBB_GLFYZZC,SW_CWBB_GLFYFZHJ,SW_CWBB_SSZBSR,SW_CWBB_WFPLRZCHJ,SW_CWBB_JLRZCHJ,SW_CWBB_YSZKYYSR,SW_CWBB_LJZJZZC,SW_CWBB_LDZCYYSR,SW_CWBB_SDSZCHJ,SW_CWBB_LJZJZJZCHJ,SW_CWBB_LRSRBL_A,SW_CWBB_XSJLL_2,SW_CWBB_YYSRYSZKPPL_A,SW_CWBB_YSZKZZL_A,SW_CWBB_GDZCBCL_A,SW_CWBB_GDZCZZL_A,SW_CWBB_MLLZZL_A,SW_CWBB_WFPLRBHL_A,SW_CWBB_LDFZYYSR_QJ,SW_CWBB_LDBL_QJ,SW_CWBB_GLFYZCHJ_QJ,SW_CWBB_JLRSYZQY_QJ,SW_CWBB_LJZJSYZQY_QJ,SW_CWBB_MLLHY,SW_CWBB_GLFZBL_QJ,SW_CWBB_SYZQY_LAST,SW_CWBB_JLRL_01S,SW_CWBB_LRB_SFQS,SW_CWBB_ZCFZB_SFQS,SW_CWBB_ZCFZB_SSQZ_MAX,SW_CWBB_ZCFZB_SSQQ_MIN,SW_CWBB_LRB_SSQZ_MAX,SW_CWBB_LRB_SSQQ_MIN,SW_CWBB_QTYSKBSSZBZBGJ,SW_CWBB_YSZKBXSSR,SW_CWBB_YSZKZZBXSSRZZ,SW_CWBB_SFYCB,SW_CWBB_YYLRZCHJ_Y,SW_CWBB_DQJKZCHJ_Y,SW_CWBB_JYYZB_ZZL_Y,SW_CWBB_YXZCFZL_QJ,SW_CWBB_HYYYSRCHB,SW_CWBB_XSQLRL_M,SW_CWBB_ZCFZL_M,SW_CWBB_MLL,SW_CWBB_QYZZL,SW_CWBB_SYZQY_ZZL_Y,SW_CWBB_CBSFQS"
    vallist=values.split(",")
    print(len(vallist))


    valia="alaba"
    print(valia.strip("a"))

    lists = os.listdir("E:\\test\\baogao\\20211013")  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime("E:\\test\\baogao\\20211013" + "\\" + fn))  # 按时间排序
    file_new = os.path.join("E:\\test\\baogao\\20211013", lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)


