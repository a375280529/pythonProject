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

def setExcelNoColor(dataset,excelpath):
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
            'bold': False,  # 字体加粗
            'text_wrap': True,  # 是否自动换行
            'valign': 'vcenter',  # 垂直对齐方式
            'align': 'left',  # 水平对齐方式
            'fg_color': 'white',  # 单元格背景颜色
            'border': 1})  # 单元格边框宽度

        qing = workbook.add_format({
            'bold': False,  # 字体加粗
            'text_wrap': True,  # 是否自动换行
            'valign': 'vcenter',  # 垂直对齐方式
            'align': 'left',  # 水平对齐方式
            'fg_color': 'white',  # 单元格背景颜色
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

def getExcelNoColor(dataset):
    img_path=forFinal.getIni("logger.ini")["model"]["saveexcelpath"]+time.strftime("%Y%m%d", time.localtime())
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    excelpath = img_path + "\\result" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".xlsx"
    setExcelNoColor(dataset, excelpath)

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
    #converters替换成dtype=str可以读取所有列为string格式
    sheet = pd.read_excel(url, sheet_name=None, converters={'nsrsbh':str,'SW_LXR_FRZJHM':str,'SW_JCXX_HY':str,'SW_JCXX_NSRZTDM':str,'GS_HYDM':str})
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
                    if str(va[i][name])=="NaT":
                        map[name] = str(None)
                    else:
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
            fg.pop("red")
        df = pd.DataFrame(gg)
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
            worksheet.write(0, col_num, value, header_format)


        #设置特定行颜色
        for index, value in ff.iterrows():
            i=0
            if value["red"]=="true":
                for va in value:
                    if va=="true":
                        pass
                    else:
                        worksheet.write(index+1, i, va, qing)
                    i+=1
            else:
                for va in value:
                    if va == "false":
                        pass
                    else:
                        worksheet.write(index+1, i, va, header_format)
                    i += 1

        #设置列宽
        worksheet.set_column("A:F", 23)
        format2 = workbook.add_format({'bold': True, 'align': 'vcenter', 'valign': 'vcenter', 'text_wrap': True})
        worksheet.set_row(0, cell_format=format2)

    writer.save()

if __name__ == '__main__':
    #数据集
    #dataset = [{'纳税编号460100196410107759，数据编号2': [{'指标名': 'SW_JCXX_CLNX', '期望值': '7.33', '实际值': '7.33', 'red': 'false'}, {'指标名': 'SW_SB_QBXSE_02Q', '期望值': '156000', '实际值': '156000', 'red': 'false'}, {'指标名': 'SW_SB_YQWSB', '期望值': '0', '实际值': '0', 'red': 'false'}]}, {'纳税编号91131121MA0C108331，数据编号3': [{'指标名': 'SW_JCXX_CLNX', '期望值': '1.45', '实际值': '1.45', 'red': 'false'}, {'指标名': 'SW_SB_SCSB', '期望值': 'None', '实际值': 'None', 'red': 'false'}, {'指标名': 'SW_CWBB_SYZQY_1', '期望值': '0', '实际值': '0', 'red': 'false'}, {'指标名': 'SW_CWBB_JLR_1', '期望值': '0', '实际值': '0', 'red': 'false'}]}, {'纳税编号91610104MA6U110392，数据编号4': [{'指标名': 'SW_JCXX_CLNX', '期望值': '2', '实际值': '2', 'red': 'false'}]}, {'纳税编号9141022100TEST0001，数据编号5': [{'指标名': 'SW_JCXX_CLNX', '期望值': 'None', '实际值': 'None', 'red': 'false'}]}, {'纳税编号91410296MA45110865，数据编号6': [{'指标名': 'SW_JCXX_HY', '期望值': '1513', '实际值': '1513', 'red': 'false'}]}, {'纳税编号9141022100TEST0002，数据编号7': [{'指标名': 'SW_JCXX_HY', '期望值': '2521', '实际值': '2521', 'red': 'false'}]}, {'纳税编号91120112MA05103951，数据编号8': [{'指标名': 'SW_JCXX_HY', '期望值': 'None', '实际值': 'None', 'red': 'false'}]}, {'纳税编号914301007279109035，数据编号9': [{'指标名': 'SW_JCXX_NSRXYPJ', '期望值': 'B', '实际值': 'B', 'red': 'false'}, {'指标名': 'SW_CWBB_SYZQY_1', '期望值': '-9287181.24', '实际值': '-9287181.24', 'red': 'false'}]}, {'纳税编号913717214942106512，数据编号10': [{'指标名': 'SW_JCXX_NSRXYPJ', '期望值': 'D', '实际值': 'D', 'red': 'false'}]}, {'纳税编号913301032554106740，数据编号11': [{'指标名': 'SW_JCXX_NSRXYPJ', '期望值': 'None', '实际值': '空', 'red': 'true'}]}, {'纳税编号914301006755109297，数据编号12': [{'指标名': 'SW_WFWZ_YZ_24M', '期望值': '0', '实际值': '0', 'red': 'false'}, {'指标名': 'SW_JCXX_NSRZTDM', '期望值': '03', '实际值': '03', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEZZL_06M', '期望值': '-0.9892', '实际值': '-0.9892', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEZZL_12M', '期望值': '-0.6297', '实际值': '-0.6297', 'red': 'false'}]}, {'纳税编号911201137736100818，数据编号13': [{'指标名': 'SW_WFWZ_YZ_24M', '期望值': '2', '实际值': '2', 'red': 'false'}]}, {'纳税编号914109235686100211，数据编号14': [{'指标名': 'SW_WFWZ_YZ_24M', '期望值': '1', '实际值': '1', 'red': 'false'}]}, {'纳税编号92610113MA6W104375，数据编号15': [{'指标名': 'SW_JCXX_NSRZTDM', '期望值': '05', '实际值': '05', 'red': 'false'}]}, {'纳税编号9141022100TEST0003，数据编号16': [{'指标名': 'SW_JCXX_NSRZTDM', '期望值': 'None', '实际值': 'None', 'red': 'false'}]}, {'纳税编号912204227445110277，数据编号17': [{'指标名': 'SW_SBZS_ZNJCS_12M_ZZSSDS', '期望值': '1', '实际值': '1', 'red': 'false'}, {'指标名': 'SW_SBZS_ZNJCS_06M_ZZSSDS', '期望值': '1', '实际值': '1', 'red': 'false'}, {'指标名': 'SW_SBZS_QS', '期望值': '1', '实际值': '1', 'red': 'false'}]}, {'纳税编号91440300MA5E101764，数据编号18': [{'指标名': 'SW_SBZS_ZNJCS_12M_ZZSSDS', '期望值': '4', '实际值': '4', 'red': 'false'}]}, {'纳税编号914211007707107556，数据编号19': [{'指标名': 'SW_SBZS_ZNJCS_12M_ZZSSDS', '期望值': '3', '实际值': '3', 'red': 'false'}]}, {'纳税编号91500109MA5U100929，数据编号20': [{'指标名': 'SW_SBZS_ZNJCS_06M_ZZSSDS', '期望值': '4', '实际值': '4', 'red': 'false'}]}, {'纳税编号913210030502100801，数据编号21': [{'指标名': 'SW_SBZS_ZNJCS_06M_ZZSSDS', '期望值': '2', '实际值': '2', 'red': 'false'}]}, {'纳税编号91341321MA2M104205，数据编号22': [{'指标名': 'SW_SBZS_YCJNCS_03M_ZZSSDS', '期望值': '2', '实际值': '2', 'red': 'false'}]}, {'纳税编号913301096998101630，数据编号23': [{'指标名': 'SW_SBZS_YCJNCS_03M_ZZSSDS', '期望值': '6', '实际值': '6', 'red': 'false'}]}, {'纳税编号91341182MA2T104824，数据编号24': [{'指标名': 'SW_SBZS_YCJNCS_03M_ZZSSDS', '期望值': '4', '实际值': '4', 'red': 'false'}]}, {'纳税编号440281198506109554，数据编号25': [{'指标名': 'SW_SBZS_QS', '期望值': '0', '实际值': '0', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEHBZZL_03M', '期望值': '2.7239', '实际值': '2.7239', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEZZL_12M', '期望值': '0.5114', '实际值': '0.5114', 'red': 'false'}, {'指标名': 'SW_SBZS_SSFK_12M', '期望值': '0', '实际值': '0', 'red': 'false'}]}, {'纳税编号91440400MA52108784，数据编号26': [{'指标名': 'SW_SB_SCSB', '期望值': '15', '实际值': '15', 'red': 'false'}]}, {'纳税编号91411624MA3X107871，数据编号27': [{'指标名': 'SW_SB_SCSB', '期望值': '10', '实际值': '10', 'red': 'false'}]}, {'纳税编号91652927MA77107194，数据编号28': [{'指标名': 'SW_SB_SCSB', '期望值': '13', '实际值': '13', 'red': 'false'}, {'指标名': 'SW_SB_LJSB0_12M', '期望值': '2', '实际值': '2', 'red': 'false'}]}, {'纳税编号911201100830109406，数据编号29': [{'指标名': 'SW_SB_NSZE_ZZSQYSDS_12M', '期望值': '3957681.25', '实际值': '3957681.25', 'red': 'false'}, {'指标名': 'SW_SB_QBXSE_12M', '期望值': '62366626.06', '实际值': '62366626.06', 'red': 'false'}, {'指标名': 'SW_SB_YQWSB', '期望值': '1', '实际值': '1', 'red': 'false'}]}, {'纳税编号91652901MA78101091，数据编号30': [{'指标名': 'SW_SB_NSZE_ZZSQYSDS_12M', '期望值': '4410.38', '实际值': '4410.38', 'red': 'false'}, {'指标名': 'SW_SB_NSZE_ZZSQYSDS_12M', '期望值': '4410.38', '实际值': '4410.38', 'red': 'false'}]}, {'纳税编号9141022100TEST0004，数据编号31': [{'指标名': 'SW_SB_NSZE_ZZSQYSDS_12M', '期望值': '15000', '实际值': '15000', 'red': 'false'}]}, {'纳税编号911200007706110062，数据编号32': [{'指标名': 'SW_CWBB_SYZQY_1', '期望值': '40384097.63', '实际值': '40384097.63', 'red': 'false'}, {'指标名': 'SW_CWBB_JLR_1', '期望值': '266914.75', '实际值': '266914.75', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEZZL_06M', '期望值': '1.7474', '实际值': '1.7474', 'red': 'false'}]}, {'纳税编号936542010978103651，数据编号33': [{'指标名': 'SW_CWBB_SYZQY_1', '期望值': 'None', '实际值': 'None', 'red': 'false'}, {'指标名': 'SW_CWBB_JLR_1', '期望值': 'None', '实际值': 'None', 'red': 'false'}, {'指标名': 'SW_SB_QBXSE_12M', '期望值': '0', '实际值': '0', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEHBZZL_03M', '期望值': 'None', '实际值': 'None', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEZZL_06M', '期望值': 'None', '实际值': 'None', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEZZL_12M', '期望值': 'None', '实际值': 'None', 'red': 'false'}]}, {'纳税编号911201121038105941，数据编号34': [{'指标名': 'SW_CWBB_JLR_1', '期望值': '-37856.77', '实际值': '-37856.77', 'red': 'false'}]}, {'纳税编号9141022100TEST0005，数据编号35': [{'指标名': 'SW_SB_QBXSE_12M', '期望值': '50000000', '实际值': '50000000', 'red': 'false'}]}, {'纳税编号93650104MA77107033，数据编号36': [{'指标名': 'SW_SB_QBXSEHBZZL_03M', '期望值': '-0.7951', '实际值': '-0.7951', 'red': 'false'}, {'指标名': 'SW_SB_QBXSEHBZZL_03M', '期望值': '-0.7951', '实际值': '-0.7951', 'red': 'false'}]}, {'纳税编号92450103MA5N100846，数据编号37': [{'指标名': 'SW_SB_QBXSEHBZZL_03M', '期望值': '-0.4', '实际值': '-0.4', 'red': 'false'}]}, {'纳税编号9141022100TEST0006，数据编号38': [{'指标名': 'SW_SB_QBXSEZZL_06M', '期望值': '-0.3', '实际值': '-0.3', 'red': 'false'}]}, {'纳税编号92140524MA0H109768，数据编号39': [{'指标名': 'SW_SB_QBXSEZZL_12M', '期望值': '-0.4', '实际值': '-0.4', 'red': 'false'}]}, {'纳税编号91131081MA0C107275，数据编号40': [{'指标名': 'SW_SBZS_XWFKCS_12M', '期望值': '0', '实际值': '0', 'red': 'false'}]}, {'纳税编号911405253536102334，数据编号41': [{'指标名': 'SW_SBZS_XWFKCS_12M', '期望值': '5', '实际值': '5', 'red': 'false'}]}, {'纳税编号91530111MA6N102003，数据编号42': [{'指标名': 'SW_SBZS_XWFKCS_12M', '期望值': '4', '实际值': '4', 'red': 'false'}]}, {'纳税编号911410817435105434，数据编号43': [{'指标名': 'SW_SBZS_SSFK_12M', '期望值': '2', '实际值': '2', 'red': 'false'}]}, {'纳税编号9141022100TEST0007，数据编号44': [{'指标名': 'SW_SBZS_SSFK_12M', '期望值': '1', '实际值': '1', 'red': 'false'}]}, {'纳税编号91652901MA77100365，数据编号45': [{'指标名': 'SW_SBZS_SSFK_12M', '期望值': '1', '实际值': '1', 'red': 'false'}]}, {'纳税编号91120112MA05110693，数据编号46': [{'指标名': 'SW_SB_ZDLXSB0_24M', '期望值': '2', '实际值': '2', 'red': 'false'}, {'指标名': 'SW_SB_QBXSE_02Q', '期望值': '0', '实际值': '0', 'red': 'false'}]}, {'纳税编号91130229MA09100765，数据编号47': [{'指标名': 'SW_SB_ZDLXSB0_24M', '期望值': '7', '实际值': '7', 'red': 'false'}]}, {'纳税编号91140302MA0K108673，数据编号48': [{'指标名': 'SW_SB_ZDLXSB0_24M', '期望值': '3', '实际值': '3', 'red': 'false'}]}, {'纳税编号91120106MA06106416，数据编号49': [{'指标名': 'SW_SB_ZDLXSB0_24M', '期望值': '3', '实际值': '3', 'red': 'false'}, {'指标名': 'SW_SB_ZDLXSB0_24M', '期望值': '2', '实际值': '2', 'red': 'false'}]}, {'纳税编号91140830MA0G101159，数据编号50': [{'指标名': 'SW_SB_ZDLXSB0_24M', '期望值': '2', '实际值': '2', 'red': 'false'}]}, {'纳税编号91130223MA07103164，数据编号51': [{'指标名': 'SW_SB_ZDLXSB0_24M', '期望值': '2', '实际值': '2', 'red': 'false'}, {'指标名': 'SW_SB_ZDLXSB0_24M', '期望值': '3', '实际值': '3', 'red': 'false'}]}]
    dataset=[{'shee1': [{'value1': 'SW_JCXX_CLNX=7.72', 'value2': 'SW_JCXX_HY=0329', 'value3': 'SW_JCXX_NSRLXDM=3', 'value4': 'SW_JCXX_NSRXYPJ=B', 'value5': 'SW_JCXX_NSRZTDM=03', 'value6': 'SW_JCXX_XZQH=6590', 'value7': 'SW_LXR_FRNL=41.0', 'value8': 'SW_LXR_FRZJHM=51303019780120**3*', 'value9': 'SW_LXR_FRXM=赖世全', 'value10': 'SW_WFWZ_12M=0', 'value11': 'SW_WFWZ_YZ_24M=0', 'value12': 'SW_JCXX_SFGTGSH=0', 'value13': 'SW_WFWZ_JJYS=99', 'value14': 'SW_BG_FRYDDH_03M=0', 'value15': 'SW_TZF_FRGDGS=0'}, {'value1': 'SW_JCXX_CLNX=5.7', 'value2': 'SW_JCXX_HY=0311', 'value3': 'SW_JCXX_NSRLXDM=3', 'value4': 'SW_JCXX_NSRXYPJ=M', 'value5': 'SW_JCXX_NSRZTDM=03', 'value6': 'SW_JCXX_XZQH=6542', 'value7': 'SW_LXR_FRNL=29.0', 'value8': 'SW_LXR_FRZJHM=65420119900607**3*', 'value9': 'SW_LXR_FRXM=杜海瑞', 'value10': 'SW_WFWZ_12M=0', 'value11': 'SW_WFWZ_YZ_24M=0', 'value12': 'SW_JCXX_SFGTGSH=0', 'value13': 'SW_WFWZ_JJYS=99', 'value14': 'SW_BG_FRYDDH_03M=0', 'value15': 'SW_TZF_FRGDGS=0'}]}]
    getExcel(dataset)
