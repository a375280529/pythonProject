# -*-coding:utf-8-*-
import stomp
import random

class SampleListener(object):
    def on_message(self, message):
        print('message: %s' % message)
        return message

def receive_from_queue(con,queuename):
    result = {}
    # 如果接受数据,就调用这个类,里面的参数是类名和类,名称必须一致
    msg=con.set_listener('SampleListener', SampleListener())
    id=random.randint(1,100)
    # 从选择的管道中区数据,管道名,id(随便写一个数字就行)
    try:
        con.subscribe(queuename, id)
        result = {"result": "True", "msg": msg}
        # 不能让程序停止,负责每传一次数据都得接收一次
        while True:
            pass
    except:
        result={"result":"False"}
    return result



def conActiveMq(host='',port=0,username='',passcode=''):
    try:
        conn=stomp.Connection([(host,port)])
        conn.connect(username=username,passcode=passcode,wait=True)
    except:
        pass
    return conn

if __name__ == '__main__':
    queuename= "vz.queue.service.collect.taxdata.xiamen"
    con=conActiveMq(host='192.168.84.230',port=61613,username='admin',passcode='admin')
    result=receive_from_queue(con,queuename)
    print(result)
    con.disconnect()