# -*- coding: utf-8 -*-

import os
import zipfile
import json
import shutil
import time
import pandas as pd

#改变xmind到zip
def replace_suffix():
    filedir = os.path.dirname(os.path.abspath(__file__))+"\\"
    files = os.listdir(filedir)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] != ".zip" and portion[1]==".xmind":
            newname = portion[0] + ".zip"
            filename = filedir + '\\' +filename
            newname = filedir + '\\' +newname
            os.rename(filename, newname)

    unpackZip(filedir)


def unpackZip(filedir):
    files = os.listdir(filedir)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".zip":
            zip_file = zipfile.ZipFile(filedir+filename)
            zip_list = zip_file.namelist()  # 得到压缩包里所有文件

            for f in zip_list:
                zip_file.extract(f, filedir)  # 循环解压文件到指定目录

            zip_file.close()  # 关闭文件，必须有，释放内存
    readJson(filedir)

def readJson(filedir):
    files = os.listdir(filedir)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".json" and portion[0] == "content":
            newname = portion[0] + ".txt"
            filename = filedir + '\\' + filename
            newname = filedir + '\\' + newname
            os.rename(filename, newname)

    readTxt(filedir)

def readTxt(filedir):
    files = os.listdir(filedir)
    result=""
    listone=[]
    listtwo=[]
    mapone={}
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".txt" and portion[0] == "content":
            with open(filedir+filename,'r', encoding='UTF-8') as f:
                result=f.readline()
    listresult=result.split("&&&&&&")[0]
    jsonresult= json.loads(listresult)
    listall=jsonresult[0]["rootTopic"]["children"]["attached"]
    zx=""
    for all in listall:
        topname=all["title"]
        aa=[]
        zxc=getFenZhi(all,zx,aa)
        for leng in zxc:
            maptwo={"用例名称":"","用例步骤":"","用例期望":""}
            lista=leng.split("@@@@@@")
            va=""
            for le in range(len(lista)):
                if le==len(lista)-1:
                    maptwo["用例期望"]=lista[le]
                elif le==len(lista)-2:
                    maptwo["用例步骤"]=lista[le]
                else:
                    va+=lista[le]+"_"
            maptwo["用例名称"]=topname+va[:-1]
            listtwo.append(maptwo)
    mapone["测试用例"]=listtwo
    listone.append(mapone)
    deleteFile(filedir)
    getExcel(listone)

#获取每个分支的拼接值
def getFenZhi(all,zx,aa):
    if "children" in all.keys():
        bb=all["children"]["attached"]
        for cc in bb:
            zx=zx+"@@@@@@"+cc["title"]
            getFenZhi(cc,zx,aa)
            zx=zx.split("@@@@@@"+zx.split("@@@@@@")[-1])[0]
    else:
        aa.append(zx)
    return aa

def deleteFile(filedir):
    files = os.listdir(filedir)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] != ".zip" and portion[1] != ".py" and portion[1]!="":
            os.remove(filedir+filename)
        elif portion[1]=="" and "2" not in portion[0]:
            shutil.rmtree(filedir+filename)

    replace_suffix_return(filedir)

def replace_suffix_return(filedir):
    files = os.listdir(filedir)
    for filename in files:
        portion = os.path.splitext(filename)

        if portion[1] != ".xmind" and portion[1]==".zip":
            newname = portion[0] + ".xmind"
            filename = filedir + '\\' +filename
            newname = filedir + '\\' +newname
            os.rename(filename, newname)


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
            'bold': False,  # 字体加粗
            'text_wrap': True,  # 是否自动换行
            'valign': 'vcenter',  # 垂直对齐方式
            'align': 'left',  # 水平对齐方式
            'fg_color': '#fffffb',  # 单元格背景颜色
            'border': 1})  # 单元格边框宽度

        qing = workbook.add_format({
            'bold': False,  # 字体加粗
            'text_wrap': True,  # 是否自动换行
            'valign': 'vcenter',  # 垂直对齐方式
            'align': 'left',  # 水平对齐方式
            'fg_color': '#fffffb',  # 单元格背景颜色
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
    img_path=os.path.dirname(os.path.abspath(__file__))+"\\"+time.strftime("%Y%m%d", time.localtime())
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    excelpath = img_path + "\\result" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".xlsx"
    setExcel(dataset, excelpath)

if __name__ == '__main__':
    replace_suffix()