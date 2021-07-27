# -*- coding: utf-8 -*-

import os
import zipfile
import shutil
import time
import pandas as pd
import getpass

#改变emmx到zip
def replace_suffix():
    filedir = os.path.dirname(os.path.abspath(__file__))+"\\"
    filedir = "D:\\emmx\\"
    files = os.listdir(filedir)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] != ".zip" and portion[1]==".emmx":
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
    filedircha=filedir+"page"
    files = os.listdir(filedircha)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".xml" and portion[0] == "page":
            newname = portion[0] + ".txt"
            filename = filedircha + '\\' + filename
            newname = filedircha + '\\' + newname
            os.rename(filename, newname)

    readTxt(filedir)

def readTxt(filedir):
    filedircha=filedir+"page"
    files = os.listdir(filedircha)
    result=""
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".txt" and portion[0] == "page":
            with open(filedircha+"\\"+filename,'r', encoding='UTF-8') as f:
                result=f.readline()
    bb = result.split('<Shape ID="101" Type="MainIdea">')
    cc = bb[1]
    dd = cc.split("</Shape>")
    array = []
    for i in range(len(dd)):
        mapa = {}
        kk = ""
        if i == 0:
            pass
        elif i == len(dd) - 1:
            pass
        else:
            ff = dd[i].split('<Shape ID="')
            gg = ff[1].split('"')
            hh = dd[i].split("</tp>")
            ii = ""
            if len(hh) > 2:
                for ei in range(len(hh)):
                    if ei == len(hh) - 1:
                        pass
                    else:
                        ii += "\n" + hh[ei].split(">")[-1]
            else:
                ii = hh[0].split(">")[-1]
            jj = dd[i].split('<SubLevel V="')
            if len(jj) <= 1:
                kk = ""
            else:
                kk = jj[1].split('"')[0]
            mapa["id"] = gg[0]
            mapa["name"] = ii
            mapa["child"] = kk
            array.append(mapa)
    indexId = ""
    retStr = ""
    alllist = []
    changelist = []
    for json in array:
        getStr(alllist, array, retStr, json, indexId)
    for zz in alllist:
        xx = zz.split("@@@@@@")
        zxc = ""
        for zx in reversed(xx):
            if zx != "":
                zxc += "@@@@@@" + zx
        changelist.append(zxc)

    mapone = {}
    listone = []
    listtwo = []
    for ali in changelist:
        maptwo = {"用例名称": "", "用例步骤": "", "用例期望": ""}
        lista = ali.split("@@@@@@")
        va = ""
        for le in range(len(lista)):
            if le == len(lista) - 1:
                maptwo["用例期望"] = lista[le]
            elif le == len(lista) - 2:
                maptwo["用例步骤"] = lista[le]
            else:
                va += lista[le] + "_"
        maptwo["用例名称"] = va[:-1][1:]
        listtwo.append(maptwo)
    mapone["测试用例"] = listtwo
    listone.append(mapone)
    deleteFile(filedir)
    getExcel(listone)

#获取每个分支的拼接值
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
                forin=0
                ci=child.split(";")
                for fid in ci:
                    if id==fid:
                        forin+=1
                if forin!=0:
                    fi=0
                    rr=retStr.split("@@@@@@")
                    for jname in rr:
                        if j["name"] == jname:
                            fi+=1
                    if fi==0:
                        retStr += "@@@@@@" + j["name"]
                        indexId += "@@@@@@" + j["child"]
                    index+=1
                    break
        if index!=0:
            getStr(alllist,array, retStr, json, indexId)
            return
        if indexId.split("@@@@@@")[1]=="":
            alllist.append(retStr)

def deleteFile(filedir):
    files = os.listdir(filedir)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] != ".zip" and portion[1] != ".py" and portion[1]!="" and portion[1]!=".exe":
            os.remove(filedir+filename)
        elif portion[1]=="" and "2" not in portion[0]:
            shutil.rmtree(filedir+filename)

    replace_suffix_return(filedir)

def replace_suffix_return(filedir):
    files = os.listdir(filedir)
    for filename in files:
        portion = os.path.splitext(filename)

        if portion[1] != ".emmx" and portion[1]==".zip":
            newname = portion[0] + ".emmx"
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
    img_path="D:\\emmx\\"+time.strftime("%Y%m%d", time.localtime())
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    excelpath = img_path + "\\result" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".xlsx"
    setExcel(dataset, excelpath)


if __name__ == '__main__':
    #inp=input("请输入密码：")
    inp=getpass.getpass("请输入密码：")
    if inp!="zc123":
        print("密码输入错误!")
        time.sleep(2)
    else:
        print("解析中...")
        replace_suffix()
        print("解析成功。")
        time.sleep(2)