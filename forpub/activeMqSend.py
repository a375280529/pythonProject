# -*-coding:utf-8-*-

import stomp

def conActiveMq(host='',port=0,username='',passcode=''):
    try:
        conn=stomp.Connection([(host,port)])
        conn.connect(username=username,passcode=passcode,wait=True)
    except:
        pass
    return conn

def send_to_queue(con,msg,queuename):
    result= {}
    # body=数据, destination=根据队列名传输数据,如果队列不存在,就创建一个
    try:
        con.send(body=str(msg), destination=queuename)
        result={"result":"True","msg":msg}
    except Exception as e:
        result={"result":"False"}
    return result

if __name__ == '__main__':
    queuename= "testmq"
    con=conActiveMq(host='127.0.0.1',port=61613,username='admin',passcode='admin')
    map={"aa":"11","bb":"22"}
    result=send_to_queue(con,map,queuename)
    print(result)
    con.disconnect()
