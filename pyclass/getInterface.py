#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import jsonpath
from suds.client import Client

def getJsonForGetInterface(url,param,headers):
    result={}
    r = requests.get(url,params=param, headers = headers)
    # 用自带的json把字符串转成字典
    try:
        dictinfo = json.loads(r.text)
        result["json"]=dictinfo
        result["code"]=r.status_code
        result["headers"] = r.headers
        result["cookies"] = r.cookies
    except:
        dictinfo = r.text
        result["json"] = dictinfo
        result["code"] = r.status_code
        result["headers"] = r.headers
        result["cookies"] = r.cookies
    return result

def getJsonForPostInterface(url,param,headers):
    result = {}
    r = requests.post(url,json=param, headers = headers)
    # 用自带的json把字符串转成字典
    try:
        dictinfo = json.loads(r.text)
        result["json"] = dictinfo
        result["code"] = r.status_code
        result["headers"] = r.headers
        result["cookies"] = r.cookies
    except:
        dictinfo = r.text
        result["json"] = dictinfo
        result["code"] = r.status_code
        result["headers"] = r.headers
        result["cookies"] = r.cookies
    return result

if __name__ == '__main__':
    # url="https://apis.juhe.cn/simpleWeather/"
    # url1="http://apis.juhe.cn/simpleWeather/query"
    # url2 = "http://localhost:8080/gateway/anhui"
    # url3="http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl"
    # url4="http://localhost:8080/vz-service-collect-henan/api/collect/preloan"
    # url5="http://192.168.86.56:8080/etaxApi/service/eTaxservice"
    # url6="http://127.0.0.1:8080/zxc"
    url7="http://data.needmone.top/sync/api/loanInfo"
    # {"areaCode": "henan", "nsrsbh": "410100",
    #  "content": {"nsrsbh": "410100", "fddbrxm": "张领", "fddbryddh": "187777", "fddbrsfzjhm": "430047013", "type": "MSG"}}
    # headers={}
    # param={}
    # content={}
    # body={}
    # data={}
    # content["nsrsbh"]="410100"
    # content["fddbrxm"] = "张领"
    # content["fddbryddh"] = "187777"
    # content["fddbrsfzjhm"] = "430047013"
    # content["type"] = "MSG"
    # # param["nsrsbh"]="U0SuR2kyJ3ERxjYfH04QQNven_D6ncmRTr5Cr03F2QI"
    # # param["yhuuid"]="gDli8cuClfHAGc7rZFR5DjcSIzNM4uu_7ReaUlfHWe62Q81tQa-vNLdFWmwb6QiU"
    # headers["appId"]="12"
    # headers["globalSerialNo"] = ""
    # headers["serviceNo"] = "credit: oper: global: search"
    # headers["dataType"] = "json"
    # headers["Content-Type"] = "application/json"
    # body["areaCode"]="henan"
    # body["nsrsbh"]="410100"
    # body["content"] = content
    # data["body"]=body
    # param["signature"]="123"
    # param["data"] = data
    # print(param)

    # pa={}
    # pa["aaa"]="1"
    # head={}
    # head["Content-Type"]="application/json"
    # ff=getJsonForPostInterface(url5,pa,head)
    # print(ff)
    # print(ff["code"])
    # print(ff["json"])

    # head={}
    # head["Content-Type"]="application/json"
    # pa={}
    # pa["username"]="tom"
    # pa["password"]="123456"
    # print(type(url6))
    # print(type(head))
    # print(type(pa))
    # ff=getJsonForPostInterface(url6,pa,head)
    # print(ff)

    head = {}
    head["Content-Type"] = "application/json"
    pa = {}
    pa["app_version"] = "1.2.2"
    pa["appversion"] = "1.2.2"
    pa["channel"] = "11"
    pa["imei"] = "11111111111"
    pa["pkg_name"] = "api"
    pa["sign"] = "aaaa"
    pa["timestamp"] = "222222"
    pa["version"] = "1.0"
    pa["application_id"] = "1020210612073836000000822"
    ff = getJsonForPostInterface(url7, pa, head)
    # print(type(ff))
    # dd=ff["json"]["appList"]
    # for ffd in dd:
    #     print(ffd["firstTime"])
    print(jsonpath.jsonpath(ff, '$..firstTime'))
    #webservice接口调用
    # url="http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl"
    # c=Client(url)
    # print(c.service.getMobileCodeInfo(""))



