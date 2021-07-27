#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

def jiekoutest():
    print(123)
    # dd=requests.get("http://1.62.154.126:8000/ajax/_Default,App_Web_default.aspx.cdcab7d2.ashx?_method=UserLogin&_session=rw")
    # list_ip = []

    url = 'http://1.62.154.126:8000/ajax/_Default,App_Web_default.aspx.cdcab7d2.ashx?_method=UserLogin&_session=rw'

    data = {

        'UserName': "123",
        'PassWord': "123123",
        'BPers_Id': False

    }

    src_data = requests.post(url, json=data)
    print(src_data)
    print(src_data.text)
    json_data = json.loads(src_data.text)

    print(json_data)
    # for i in json_data["data"]:
    #
    #     if i["run_type"] == run_type:
    #         list_ip.append(i["ip"])
    #
    # return list_ip

if __name__ == '__main__':
    jiekoutest()