#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

import pandas as pd
import time
import os
import datetime
from forpub import forFinal
import numpy as nm

def setExcel(dataset,excelpath):
    # 创建excelwriter对象
    writer = pd.ExcelWriter(excelpath, engine='xlsxwriter')
    for data in range(len(dataset)):
        # 生成dataframe
        df = pd.DataFrame(dataset[data].get(list(dataset[data].keys())[0]))
        # # 生成excel
        # df.to_excel(excelpath, sheet_name=list(dataset[data].keys())[0], index=None)

        # 设置excel
        df.to_excel(writer, sheet_name=list(dataset[data].keys())[0], startrow=1, header=0, index=False)

        workbook = writer.book
        worksheet = writer.sheets[list(dataset[data].keys())[0]]
        header_format = workbook.add_format({
            'bold': True,  # 字体加粗
            'text_wrap': True,  # 是否自动换行
            'valign': 'vcenter',  # 垂直对齐方式
            'align': 'vcenter',  # 水平对齐方式
            'fg_color': '#faa755',  # 单元格背景颜色
            'border': 2})  # 单元格边框宽度

        qing = workbook.add_format({
            'bold': False,  # 字体加粗
            'text_wrap': True,  # 是否自动换行
            'valign': 'vcenter',  # 垂直对齐方式
            'align': 'right',  # 水平对齐方式
            'fg_color': '#50b7c1',  # 单元格背景颜色
            'border': 1})  # 单元格边框宽度


        #设置第一列每行的颜色
        for col_num, value in enumerate(df.columns.values):
            if col_num % 2 == 0:
                worksheet.write(0, col_num, value, header_format)
            else:
                worksheet.write(0, col_num, value, qing)


        #设置第一行每列的颜色
        for index, value in df.iterrows():
            i = 0
            for va in value:
                if i == 0:
                    worksheet.write(index + 1, i, va, header_format)
                else:
                    worksheet.write(index + 1, i, va, qing)
                i += 1

        #设置列宽
        worksheet.set_column("A:F", 23)
        format2 = workbook.add_format({'bold': True, 'align': 'vcenter', 'valign': 'vcenter', 'text_wrap': True})
        worksheet.set_row(0, cell_format=format2)

    writer.save()


def getExcel(dataset):
    img_path=forFinal.getIni("logger.ini")["model"]["saveexcelpath"]+time.strftime("%Y%m%d", time.localtime())
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    excelpath = img_path + "\\result" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".xlsx"
    setExcel(dataset, excelpath)

def readExcel(url):
    xl = pd.ExcelFile(url)
    df = xl.parse(0)
    list = []
    for i in range(len(df)):
        map = {}
        for name in df:
            if isinstance(df[name][i],str):
                map[name] = df[name][i]
            elif isinstance(df[name][i],datetime.datetime):
                map[name] = datetime.datetime.strftime(df[name][i],'%Y/%m/%d')
            else:
                if str(df[name][i])=="nan":
                    map[name] = str(None)
                else:
                    map[name] = str(df[name][i])
        list.append(map)
    return list

#读取原始单元格格式的excel
def readExcelRealGeShi(url):
    xl = pd.ExcelFile(url)
    df = xl.parse(0)
    list = []
    for i in range(len(df)):
        map = {}
        for name in df:
            if isinstance(df[name][i],str):
                map[name] = df[name][i]
            elif isinstance(df[name][i],datetime.datetime):
                map[name] = datetime.datetime.strftime(df[name][i],'%Y/%m/%d')
            elif isinstance(df[name][i], nm.integer):
                map[name] = int(df[name][i])
            elif isinstance(df[name][i], nm.floating):
                if str(df[name][i])=="nan":
                    map[name] = None
                else:
                    map[name] = float(df[name][i])
            else:
                if str(df[name][i])=="nan":
                    map[name] = None
                else:
                    map[name] = df[name][i]
        list.append(map)
    return list

#读取excel的所有sheet
def readExcelSheet(url):
    sheet = pd.read_excel(url, sheet_name=None, converters={'nsrsbh':str})
    listall=[]
    for va in sheet.values():
        va = va.to_dict(orient='records')
        list = []
        for i in range(len(va)):
            map = {}
            for name in va[i].keys():
                if isinstance(va[i][name], str):
                    map[name] = va[i][name]
                elif isinstance(va[i][name], datetime.datetime):
                    map[name] = datetime.datetime.strftime(va[i][name], '%Y/%m/%d')
                elif isinstance(va[i][name], float):
                    if str(va[i][name]) == "nan":
                        map[name] = str(None)
                    else:
                        map[name]=str(va[i][name])
                    #map[name]='{:g}'.format(va[i][name])
                else:
                    if str(va[i][name]) == "nan":
                        map[name] = str(None)
                    else:
                        map[name] = str(va[i][name])
            list.append(map)
        listall.append(list)
    return listall

#生成带颜色标记的excel
def getExcelColor(dataset):
    img_path=forFinal.getIni("logger.ini")["model"]["saveexcelpath"]+time.strftime("%Y%m%d", time.localtime())
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    excelpath = img_path + "\\result" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".xlsx"
    setExcelColor(dataset, excelpath)

#生成带颜色标记的excel
def setExcelColor(dataset,excelpath):
    # 创建excelwriter对象
    writer = pd.ExcelWriter(excelpath, engine='xlsxwriter')
    for data in range(len(dataset)):
        ff = pd.DataFrame(dataset[data].get(list(dataset[data].keys())[0]))
        gg=dataset[data].get(list(dataset[data].keys())[0])
        # 生成dataframe
        for fg in gg:
            fg.pop("$颜色")
        df = pd.DataFrame(gg)
        # # 生成excel
        # df.to_excel(excelpath, sheet_name=list(dataset[data].keys())[0], index=None)
        # 设置excel
        df.to_excel(writer, sheet_name=list(dataset[data].keys())[0], startrow=1, header=0, index=False)

        workbook = writer.book
        worksheet = writer.sheets[list(dataset[data].keys())[0]]
        header_format = workbook.add_format({
            'bold': False,  # 字体加粗
            'text_wrap': True,  # 是否自动换行
            'valign': 'vcenter',  # 垂直对齐方式
            'align': 'vcenter',  # 水平对齐方式
            'border': 1})  # 单元格边框宽度

        qing = workbook.add_format({
            'bold': False,  # 字体加粗
            'text_wrap': True,  # 是否自动换行
            'valign': 'vcenter',  # 垂直对齐方式
            'align': 'vcenter',  # 水平对齐方式
            'fg_color': 'red',  # 单元格背景颜色
            'border': 1})  # 单元格边框宽度

        #设置第一行数据
        for col_num, value in enumerate(df.columns.values):
            if value == "$颜色":
                pass
            else:
                worksheet.write(0, col_num, value, header_format)


        #设置特定行颜色
        for index, value in ff.iterrows():
            i=-1
            if value[0]=="$红":
                for va in value:
                    if va=="$红":
                        pass
                    else:
                        worksheet.write(index + 1, i, va, qing)
                    i+=1
            else:
                for va in value:
                    if va == "$无":
                        pass
                    else:
                        worksheet.write(index + 1, i, va, header_format)
                    i += 1

        #设置列宽
        worksheet.set_column("A:F", 23)
        format2 = workbook.add_format({'bold': True, 'align': 'vcenter', 'valign': 'vcenter', 'text_wrap': True})
        worksheet.set_row(0, cell_format=format2)

    writer.save()

if __name__ == '__main__':
    # 数据集
    dataset = [{"123456":[
        {"$颜色":"$无","姓名": "张三zzzzzzzzzzzzzzzzzzz", "年龄": "zzzzzzzzzz123", "性别": "zzzzzzzzzzzzzzz男"},
        {"$颜色":"$无","姓名": "李四xxxxxxxxxxxxxxxxxxx", "年龄": "xxxxxxxxxxxx234", "性别": "xxxxxxxxxxxxxxxx男"},
        {"$颜色":"$红","姓名": "王五ccccccccccccccccccc", "年龄": "cccccccccccc345", "性别": "cccccccccccccc女"}
    ]},{"987654321":[
        {"$颜色":"$无","姓名": "陈六qqqqqqqqqqqqqqqqqqq", "年龄": "qqqqqqqqqqqq456", "性别": "qqqqqqqqqqqqq女"},
        {"$颜色":"$红","姓名": "刘七wwwwwwwwwwwwwwwwwww", "年龄": "wwwwwwwwwwww567", "性别": "wwwwwwwwwwwwww男"},
        {"$颜色":"$红","姓名": "赵八eeeeeeeeeeeeeeeeeee", "年龄": "eeeeeeeeeeee678", "性别": "eeeeeeeeeeeeee女"}
    ]}]
    getExcelColor(dataset)