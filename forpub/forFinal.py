#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import configparser
import random
import pandas as pd
from xml.dom.minidom import parse
import base64
import logging
import hashlib
import json
import xmltodict
from bs4 import BeautifulSoup
import paramiko
import sys
import time
from urllib.parse import urlencode, quote, unquote

# 获取配置文件相对路径
def getIniPath():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path.split(path.split('\\')[-1])[0] + "iniFile" + "\\"
    # exepath = os.path.realpath(sys.executable)
    # endpath = exepath.split(exepath.split("\\")[-1])[0]
    # path = os.path.join(os.path.abspath('.'), endpath + "iniFile\\")
    return path


# 读取配置文件的方法，ini为配置文件名称
def readini(ini):
    path = getIniPath() + ini
    config = configparser.ConfigParser()
    config.read(path,encoding="utf-8-sig")
    return config


# 获取日志文件相对路径
def getLogPath():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path.split(path.split('\\')[-1])[0] + "logFile" + "\\"
    return path

#随机数
def haveIntRondom():
    top=random.randint(10000000000, 99999999999)
    return top

#读取ini配置文件数据
def getIni(ini):
    config = readini(ini)
    return config

#解决乱码
def statement(value):
    data = value.encode("utf-8").decode("utf-8")
    return data

#解决网页返回信息乱码
def statementPage(value):
    data=value.encode("raw_unicode_escape").decode()
    return data

#返回xml根节点
def readXml():
    domTree=parse(os.path.abspath(os.path.join(os.getcwd(), ".."))+"/xmlFile/xmlfile.xml")
    # 文档根元素
    rootNode = domTree.documentElement
    return rootNode

#根据name读取xml中不同环境的数据库信息
def getXmlNode(name):
    map={}
    node=readXml()
    print(node.nodeName)
    tagname=node.getElementsByTagName("name")
    for tname in tagname:
        if tname.hasAttribute("bname"):
            bsname=tname.getAttribute("bname")
            if bsname==name:
                connectname=tname.getElementsByTagName("connectname")[0].childNodes[0].data
                connectpassword = tname.getElementsByTagName("connectpassword")[0].childNodes[0].data
                connectip = tname.getElementsByTagName("connectip")[0].childNodes[0].data
                dbname = tname.getElementsByTagName("dbname")[0].childNodes[0].data
                map["connectname"]=connectname
                map["connectpassword"] = connectpassword
                map["connectip"] = connectip
                map["dbname"] = dbname
                return map

#读取excel所有sheet
def readAllExcelSheet():
    sheet = pd.read_excel("E:\\test\\newgo.xlsx", sheet_name=None)
    #所有sheet的名称
    for j in sheet.keys():
        print(j)
    #每个sheet中所有数据信息
    for j1 in sheet.values():
        j1 = j1.to_dict(orient='records')
        print(j1)
    #sheet名称与数据信息键值对形式
    for k, v in sheet.items():
        v = v.to_dict(orient='records')
        print(k, v)

#判断是否全是中文
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

#检验是否含有中文字符
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

#使用base64加密
def encryption_base64(str_cont):
    bytes_cont = str_cont.encode("utf-8")
    result = base64.b64encode(bytes_cont)
    return result


#解密base64格式的文本
def decrypt_base64(str_cont):
    result = base64.b64decode(str_cont).decode("utf-8")
    return result

#进度条，循环里面需要加上time.sleep(0.001)，percent是未转成百分比的小数,循环到最后的时候赋值为1（for i in range(10000);time.sleep(0.001);a=(i+1)/10000;progress(a)）
def progress(percent):
    if percent > 1:
        percent = 1
    res = int(50 * percent) * '>'
    print('\r[%-50s] %d%%' % (res, int(100 * percent)), end='')

#数组进行冒泡排序,从小到大
def maopao(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

#去除小数点末尾的0，val为str
def quzero(val):
    try:
        #dex=val.index('.')
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

#用于四舍五入 value:值(float类型) weishu(保留几位)
def newround(value,weishu):
    biaoshi=0
    if str(value)[0]=="-":
        value=-value
        biaoshi=1
    strvalue = str(value)
    va=strvalue.split(".")
    if len(va)==1:
        if biaoshi==1:
            return float("-"+va[0])
        else:
            return float(va[0])
    if weishu>=len(va[1]):
        if biaoshi==1:
            return float("-"+strvalue)
        else:
            return float(strvalue)
    if len(va) != 1:
        if weishu==0:
            if int(va[1][weishu])>=5:
                result=float(int(va[0])+1)
            else:
                result=float(int(va[0]))
        elif weishu==1:
            if int(va[1][weishu])>=5:
                result=float(va[0] +"."+str(int(va[1][weishu-1])+1))
            else:
                result=float(va[0] + "." + str(int(va[1][weishu - 1])))
        else:
            if int(va[1][weishu])>=5:
                xiaoshuwei=str(int(va[1][:weishu])+1)
                if xiaoshuwei[0]=="1" and va[1][0]!="1":
                    result=float(int(va[0]) +1)
                else:
                    result = float(va[0] + "." + str(int(va[1][:weishu]) + 1))
            else:
                result=float(va[0] + "." +str(int(va[1][:weishu - 1]))+ str(int(va[1][weishu - 1])))
    if biaoshi==1:
        result=-result
    return result

#更改ini中对应的key的值，ini为ini的文件名称，title为最外面名称,key为键，value为值
def writeIni(ini,title,key,value):
    path = getIniPath() + ini
    fixConfig = configparser.ConfigParser(comment_prefixes='/', allow_no_value=True)
    #comment_prefixes='/', allow_no_value=True可以保留Ini的注释，异常字符时候用RawConfigParser
    #fixConfig = configparser.RawConfigParser(comment_prefixes='/', allow_no_value=True)
    fixConfig.read(path, encoding="utf-8-sig")
    fixConfig.set(title, key, value)
    with open(path, "w+", encoding="utf-8-sig") as f:
        fixConfig.write(f)
        f.close()

#stringvalue为str类型，把unicode转字符串（\\u64cd\\u4f5c\\u6210\\u529f）
def unicodetostr(stringvalue):
    re=stringvalue.encode("utf-8").decode("unicode_escape")
    return re

#md5加密
def strformd5(text):
    hl=hashlib.md5()
    hl.update(text.encode(encoding="utf-8"))
    md5value=hl.hexdigest()
    return md5value

#上传文件到sftp
def uploadsftp(filename):
    ini = getIni("loggerTable.ini")
    ip = ini["callpro"]["callproConnect_sftp_ip"]
    port = int(ini["callpro"]["callproConnect_sftp_port"])
    username = ini["callpro"]["callproConnect_sftp_username"]
    password = ini["callpro"]["callproConnect_sftp_password"]
    path = ini["callpro"]["callproConnect_sftp__path"]
    handle = paramiko.Transport((ip,port))
    handle.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(handle)
    sftpfile=path_replace("sftpfile/"+filename)
    sftp.put(sftpfile,path+"/"+filename)

#xml转json
def changexmltojson(xml):
    soup = BeautifulSoup(xml, 'xml')
    hh = xmltodict.parse(str(soup))
    di = json.dumps(dict(hh))
    js = json.loads(di)
    return js

#win和Linux路径的转换
def path_replace(filename):
    #（打包需要更换）
    path = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = path.split(path.split('\\')[-1])[0]
    # exepath = os.path.realpath(sys.executable)
    # endpath = exepath.split(exepath.split("\\")[-1])[0]
    # BASE_DIR = os.path.join(os.path.abspath('.'), endpath)
    if 'win' in sys.platform:
        filename=filename.replace("/","\\")
        r=BASE_DIR+filename
    else:
        r=BASE_DIR+filename
    return r

#读取json文件
def build_data(filepath):
    # 1. with open() 只读方式，打开文件，获取文件对象
    with open(filepath, 'r', encoding='utf-8') as f:
        # 2. 调用方法获取文件内容：读取的内容 = json.load(文件对象)
        json_data = json.load(f)
        # print(json_data)
    return json_data

#初始化日志
def init_log_config(filename, when='midnight', interval=1, backup_count=7):

    # 1. 创建日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 3. 创建处理器对象
    # 输出到控制台
    st = logging.StreamHandler()
    # 输出到日志文件
    # when 是一个字符串，定义了日志切分的间隔时间单位
    # interval 是间隔时间单位的个数，指等待多少个 when 的时间后继续进行日志记录
    # backupCount 是保留日志的文件个数
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when=when,
                                                   interval=interval,
                                                   backupCount=backup_count,
                                                   encoding='utf-8')

    # 4. 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 5. 给处理器设置格式化器
    st.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 6. 给日志器添加处理器
    logger.addHandler(st)
    logger.addHandler(fh)

#对url后面参数进行解码（如参数%E6%98%AF）
def unquotetostr(str):
    return unquote(str)

if __name__ == '__main__':
    # # 1:获取当前时间并整理格式
    # lognow = time.strftime("%Y%m%d", time.localtime(time.time()))
    # # 初始化日志
    # log_path = path_replace('/log/' + lognow + '.log')
    # init_log_config(log_path)
    aa=unquotetostr("%E6%98%AF")
    print(aa)
