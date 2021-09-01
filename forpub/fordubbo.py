import extend

def connectDubbo():
    df=input()
    if df=="1":
        ff="{'ff':'ss'}"
        data = {
            'service': "com.ustc.demo.provider.DemoService",
            'method': "sayHello",
            'args': '"'+ff+'"'
        }
    else:
        ff = "{'signature':'','data':{'body':{'areaCode':'chongqing','nsrsbh':'912*********65L','content':{'nsrsbh':'912*********65L','cpbm':'A001'}},'head':" \
             "{'appId':'','globalSerialNo':'','serviceNo':'credit:oper:global:search','dataType':'json'}}}"
        data = {
            'service': "com.vzoom.zxxt.facade.tianjin.ItianjinService",
            'method': "requestCollectSub",
            'args': '"' + ff + '"'
        }


    zk = extend.ZooKeeper('192.168.85.112:2181')
    info = zk.getDubboInfo(data['service'])
    try:
        res, data['invoke_time'] = extend.dubboTelnet(
            info['host'], info['port'], data['service'], data['method'], data['args'])
        invoke_time=data['invoke_time']
        if invoke_time==False:
            print("erro")
            print(res)
        else:
            print("success")
            print(res)
    except Exception as errorMsg:
        print(errorMsg)
    zk.disconnect()

if __name__ == '__main__':
    connectDubbo()